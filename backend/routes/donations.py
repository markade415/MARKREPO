from fastapi import APIRouter, HTTPException, Request, Header
from typing import List, Optional
import os
from datetime import datetime, timedelta
from emergentintegrations.payments.stripe.checkout import StripeCheckout, CheckoutSessionRequest, CheckoutSessionResponse, CheckoutStatusResponse
from motor.motor_asyncio import AsyncIOMotorClient
import logging

from models import (
    DonationCreate,
    Donation,
    CampaignStats,
    RecentDonation,
    StripeSessionCreate,
    StripeSessionResponse,
    StripeStatusResponse,
    PayPalOrderCreate,
    PayPalOrderResponse,
    PayPalCaptureResponse
)

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/donations", tags=["donations"])

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Stripe configuration
STRIPE_API_KEY = os.environ.get('STRIPE_API_KEY', 'sk_test_emergent')

# Helper function to get or create campaign stats
async def get_campaign_stats():
    stats = await db.campaign_stats.find_one({"campaign_name": "RocketShip Mission"})
    if not stats:
        # Initialize with seed data
        initial_stats = {
            "campaign_name": "RocketShip Mission",
            "goal": 18500.00,
            "current_amount": 12000.00,
            "donor_count": 187,
            "percent_complete": 64.9,
            "last_updated": datetime.utcnow()
        }
        await db.campaign_stats.insert_one(initial_stats)
        stats = initial_stats
    return stats

# Helper function to update campaign stats
async def update_campaign_stats(amount: float):
    stats = await get_campaign_stats()
    new_amount = stats['current_amount'] + amount
    new_donor_count = stats['donor_count'] + 1
    new_percent = round((new_amount / stats['goal']) * 100, 1)
    
    await db.campaign_stats.update_one(
        {"campaign_name": "RocketShip Mission"},
        {
            "$set": {
                "current_amount": new_amount,
                "donor_count": new_donor_count,
                "percent_complete": new_percent,
                "last_updated": datetime.utcnow()
            }
        }
    )

# Stripe Endpoints
@router.post("/stripe/create-session", response_model=StripeSessionResponse)
async def create_stripe_session(data: StripeSessionCreate, request: Request):
    try:
        # Get the host URL from the request
        host_url = str(request.base_url).rstrip('/')
        
        # Create success and cancel URLs
        success_url = f"{host_url}/donation-success?session_id={{CHECKOUT_SESSION_ID}}"
        cancel_url = f"{host_url}/donation-cancelled"
        
        # Initialize Stripe checkout
        webhook_url = f"{host_url}/api/webhook/stripe"
        stripe_checkout = StripeCheckout(api_key=STRIPE_API_KEY, webhook_url=webhook_url)
        
        # Create checkout session
        checkout_request = CheckoutSessionRequest(
            amount=data.amount,
            currency="usd",
            success_url=success_url,
            cancel_url=cancel_url,
            metadata={
                "tier_id": data.tier_id or "",
                "campaign": "RocketShip Mission"
            }
        )
        
        session: CheckoutSessionResponse = await stripe_checkout.create_checkout_session(checkout_request)
        
        # Create pending donation record
        donation = Donation(
            amount=data.amount,
            currency="usd",
            payment_method="stripe",
            payment_status="pending",
            session_id=session.session_id,
            tier_id=data.tier_id,
            metadata={"tier_id": data.tier_id or ""}
        )
        
        await db.donations.insert_one(donation.dict())
        
        return StripeSessionResponse(url=session.url, session_id=session.session_id)
        
    except Exception as e:
        logger.error(f"Error creating Stripe session: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to create payment session: {str(e)}")

@router.get("/stripe/status/{session_id}", response_model=StripeStatusResponse)
async def get_stripe_status(session_id: str, request: Request):
    try:
        # Initialize Stripe checkout
        host_url = str(request.base_url).rstrip('/')
        webhook_url = f"{host_url}/api/webhook/stripe"
        stripe_checkout = StripeCheckout(api_key=STRIPE_API_KEY, webhook_url=webhook_url)
        
        # Get checkout status
        status: CheckoutStatusResponse = await stripe_checkout.get_checkout_status(session_id)
        
        # Find the donation record
        donation = await db.donations.find_one({"session_id": session_id})
        
        if donation:
            # Check if already processed
            if donation['payment_status'] == 'completed' and status.payment_status == 'paid':
                # Already processed, don't update stats again
                return StripeStatusResponse(
                    status=status.status,
                    payment_status=status.payment_status,
                    amount=status.amount_total / 100,  # Convert from cents
                    currency=status.currency
                )
            
            # Update donation status
            if status.payment_status == 'paid' and donation['payment_status'] != 'completed':
                await db.donations.update_one(
                    {"session_id": session_id},
                    {
                        "$set": {
                            "payment_status": "completed",
                            "updated_at": datetime.utcnow()
                        }
                    }
                )
                # Update campaign stats
                await update_campaign_stats(donation['amount'])
            elif status.status == 'expired':
                await db.donations.update_one(
                    {"session_id": session_id},
                    {
                        "$set": {
                            "payment_status": "cancelled",
                            "updated_at": datetime.utcnow()
                        }
                    }
                )
        
        return StripeStatusResponse(
            status=status.status,
            payment_status=status.payment_status,
            amount=status.amount_total / 100,  # Convert from cents
            currency=status.currency
        )
        
    except Exception as e:
        logger.error(f"Error getting Stripe status: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to get payment status: {str(e)}")

# Campaign Stats Endpoints
@router.get("/stats", response_model=CampaignStats)
async def get_stats():
    try:
        stats = await get_campaign_stats()
        return CampaignStats(**stats)
    except Exception as e:
        logger.error(f"Error getting campaign stats: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to get campaign stats: {str(e)}")

# Recent Donations Endpoint
@router.get("/recent", response_model=List[RecentDonation])
async def get_recent_donations():
    try:
        # Get completed donations, sorted by date
        donations = await db.donations.find(
            {"payment_status": "completed"}
        ).sort("created_at", -1).limit(10).to_list(10)
        
        recent = []
        for donation in donations:
            # Calculate time ago
            time_diff = datetime.utcnow() - donation['created_at']
            if time_diff.days > 0:
                time_str = f"{time_diff.days} day{'s' if time_diff.days > 1 else ''} ago"
            elif time_diff.seconds // 3600 > 0:
                hours = time_diff.seconds // 3600
                time_str = f"{hours} hour{'s' if hours > 1 else ''} ago"
            else:
                minutes = time_diff.seconds // 60
                time_str = f"{minutes} minute{'s' if minutes > 1 else ''} ago"
            
            recent.append(RecentDonation(
                name=donation.get('donor_name', 'Anonymous'),
                amount=donation['amount'],
                time=time_str
            ))
        
        return recent
    except Exception as e:
        logger.error(f"Error getting recent donations: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to get recent donations: {str(e)}")