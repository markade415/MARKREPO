# RocketShip Fundraising Backend Integration Contract

## Overview
This document outlines the integration plan for connecting the frontend landing page with backend payment processing (Stripe & PayPal) and MongoDB database.

## Current State (Frontend with Mock Data)
- Landing page with hero section, progress tracker, donation tiers
- Donation form with Stripe/PayPal selection
- Mock data in `/app/frontend/src/mock.js`
- Campaign goal: $18,500
- Current raised: $12,000 (64.9%)
- Mock donation function simulates payment

## Backend Implementation Plan

### 1. Database Models (MongoDB)

#### Collection: `donations`
```javascript
{
  _id: ObjectId,
  amount: Float (e.g., 25.00),
  currency: String ("usd"),
  payment_method: String ("stripe" | "paypal"),
  payment_status: String ("pending" | "completed" | "failed" | "cancelled"),
  session_id: String (Stripe session ID or PayPal order ID),
  donor_name: String (optional),
  donor_email: String (optional),
  tier_id: String (optional, e.g., "tier1"),
  metadata: Object,
  created_at: DateTime,
  updated_at: DateTime
}
```

#### Collection: `campaign_stats`
```javascript
{
  _id: ObjectId,
  campaign_name: "RocketShip Mission",
  goal: Float (18500.00),
  current_amount: Float (12000.00),
  donor_count: Integer,
  last_updated: DateTime
}
```

### 2. Backend API Endpoints

#### Stripe Integration
- `POST /api/donations/stripe/create-session`
  - Input: `{ amount: Float, tier_id: String (optional) }`
  - Returns: `{ url: String, session_id: String }`
  - Creates Stripe checkout session
  - Creates pending donation record

- `GET /api/donations/stripe/status/:sessionId`
  - Returns: `{ status: String, payment_status: String, amount: Float }`
  - Polls Stripe for payment status
  - Updates donation record

- `POST /api/webhook/stripe`
  - Handles Stripe webhooks
  - Updates donation status
  - Updates campaign stats

#### PayPal Integration
- `POST /api/donations/paypal/create-order`
  - Input: `{ amount: Float, tier_id: String (optional) }`
  - Returns: `{ order_id: String }`
  - Creates PayPal order
  - Creates pending donation record

- `POST /api/donations/paypal/capture/:orderId`
  - Captures PayPal payment
  - Updates donation record
  - Updates campaign stats

#### Campaign Data
- `GET /api/campaign/stats`
  - Returns: `{ goal: Float, current_amount: Float, donor_count: Integer, percent_complete: Float }`
  - Real-time campaign progress

- `GET /api/donations/recent`
  - Returns: Array of recent donations
  - Limited to last 10-20 donations

### 3. Frontend Integration Changes

#### Remove Mock Data Usage
- Remove `mockDonation` function calls
- Replace with real API calls to backend

#### DonationForm.jsx Changes
1. On form submit (Stripe):
   - Call `POST /api/donations/stripe/create-session`
   - Redirect to Stripe checkout URL
   - On return, poll `GET /api/donations/stripe/status/:sessionId`
   - Show success/failure message

2. On form submit (PayPal):
   - Call `POST /api/donations/paypal/create-order`
   - Use PayPal SDK to show checkout
   - On approval, call `POST /api/donations/paypal/capture/:orderId`
   - Show success/failure message

#### LandingPage.jsx Changes
1. Fetch real campaign stats:
   - `useEffect` to call `GET /api/campaign/stats`
   - Update progress tracker with real data

2. Fetch recent donations:
   - Call `GET /api/donations/recent`
   - Display in "Recent Supporters" section

### 4. Security & Configuration

- Store Stripe API key in `/app/backend/.env`: `STRIPE_API_KEY=sk_test_emergent`
- Store PayPal credentials in `/app/backend/.env`: `PAYPAL_CLIENT_ID` and `PAYPAL_SECRET`
- Use emergentintegrations library for Stripe (already available)
- PayPal SDK for PayPal integration

### 5. Payment Flow

#### Stripe Flow:
1. User fills form → clicks "Donate"
2. Frontend calls `/api/donations/stripe/create-session`
3. Backend creates Stripe session + pending donation record
4. Frontend redirects to Stripe checkout
5. User completes payment on Stripe
6. Stripe redirects back with `session_id`
7. Frontend polls `/api/donations/stripe/status/:sessionId`
8. Backend updates donation status to "completed"
9. Campaign stats updated
10. Success message shown

#### PayPal Flow:
1. User fills form → clicks "Donate"
2. Frontend calls `/api/donations/paypal/create-order`
3. Backend creates PayPal order + pending donation record
4. Frontend shows PayPal checkout modal
5. User approves payment
6. Frontend calls `/api/donations/paypal/capture/:orderId`
7. Backend captures payment and updates donation status
8. Campaign stats updated
9. Success message shown

### 6. Initial Data Seeding

Seed `campaign_stats` collection with:
```javascript
{
  campaign_name: "RocketShip Mission",
  goal: 18500.00,
  current_amount: 12000.00,
  donor_count: 187,
  last_updated: new Date()
}
```

Seed some sample donations to show in "Recent Supporters"

## Implementation Order
1. ✅ Frontend with mock data (COMPLETED)
2. Install emergentintegrations library
3. Create MongoDB models in backend
4. Create Stripe endpoints
5. Create PayPal endpoints
6. Create campaign stats endpoints
7. Update frontend to use real APIs
8. Test payment flows
9. Seed initial data
10. Final testing
