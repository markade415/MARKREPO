from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid

# Donation Models
class DonationCreate(BaseModel):
    amount: float = Field(..., description="Donation amount in dollars")
    tier_id: Optional[str] = Field(None, description="Donation tier ID")
    donor_name: Optional[str] = Field(None, description="Donor name")
    donor_email: Optional[str] = Field(None, description="Donor email")

class Donation(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    amount: float
    currency: str = "usd"
    payment_method: str  # "stripe" or "paypal"
    payment_status: str = "pending"  # "pending", "completed", "failed", "cancelled"
    session_id: str  # Stripe session ID or PayPal order ID
    tier_id: Optional[str] = None
    donor_name: Optional[str] = None
    donor_email: Optional[str] = None
    metadata: Optional[dict] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class CampaignStats(BaseModel):
    campaign_name: str = "RocketShip Mission"
    goal: float = 18500.00
    current_amount: float = 0.00
    donor_count: int = 0
    percent_complete: float = 0.0
    last_updated: datetime = Field(default_factory=datetime.utcnow)

class RecentDonation(BaseModel):
    name: str
    amount: float
    time: str

# Stripe Models
class StripeSessionCreate(BaseModel):
    amount: float
    tier_id: Optional[str] = None

class StripeSessionResponse(BaseModel):
    url: str
    session_id: str

class StripeStatusResponse(BaseModel):
    status: str
    payment_status: str
    amount: float
    currency: str

# PayPal Models
class PayPalOrderCreate(BaseModel):
    amount: float
    tier_id: Optional[str] = None

class PayPalOrderResponse(BaseModel):
    order_id: str
    approval_url: str

class PayPalCaptureResponse(BaseModel):
    order_id: str
    status: str
    amount: float