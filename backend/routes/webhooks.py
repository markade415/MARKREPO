from fastapi import APIRouter, Request, HTTPException
import os
import logging
from emergentintegrations.payments.stripe.checkout import StripeCheckout
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/webhook", tags=["webhooks"])

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Stripe configuration
STRIPE_API_KEY = os.environ.get('STRIPE_API_KEY', 'sk_test_emergent')

@router.post("/stripe")
async def stripe_webhook(request: Request):
    try:
        # Get webhook body and signature
        body = await request.body()
        signature = request.headers.get("Stripe-Signature")
        
        if not signature:
            logger.warning("No Stripe signature found in webhook request")
            return {"status": "no_signature"}
        
        # Initialize Stripe checkout
        host_url = str(request.base_url).rstrip('/')
        webhook_url = f"{host_url}/api/webhook/stripe"
        stripe_checkout = StripeCheckout(api_key=STRIPE_API_KEY, webhook_url=webhook_url)
        
        # Handle webhook
        webhook_response = await stripe_checkout.handle_webhook(body, signature)
        
        logger.info(f"Webhook event: {webhook_response.event_type}")
        
        # Process payment completed events
        if webhook_response.event_type == "checkout.session.completed":
            session_id = webhook_response.session_id
            
            # Find donation
            donation = await db.donations.find_one({"session_id": session_id})
            
            if donation and donation['payment_status'] != 'completed':
                # Update donation status
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
                stats = await db.campaign_stats.find_one({"campaign_name": "RocketShip Mission"})
                if stats:
                    new_amount = stats['current_amount'] + donation['amount']
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
                
                logger.info(f"Payment completed for session {session_id}")
        
        return {"status": "processed"}
        
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        return {"status": "error", "message": str(e)}
