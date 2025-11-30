#!/usr/bin/env python3
"""
Backend API Testing for RocketShip Fundraising Campaign
Tests all donation-related endpoints and Stripe integration
"""

import asyncio
import aiohttp
import json
import os
from datetime import datetime
import sys

# Get backend URL from frontend .env file
def get_backend_url():
    try:
        with open('/app/frontend/.env', 'r') as f:
            for line in f:
                if line.startswith('REACT_APP_BACKEND_URL='):
                    return line.split('=', 1)[1].strip()
    except Exception as e:
        print(f"Error reading frontend .env: {e}")
        return None

BACKEND_URL = get_backend_url()
if not BACKEND_URL:
    print("ERROR: Could not find REACT_APP_BACKEND_URL in frontend/.env")
    sys.exit(1)

API_BASE = f"{BACKEND_URL}/api"

class TestResults:
    def __init__(self):
        self.results = []
        self.session_id = None
        
    def add_result(self, test_name, success, message, details=None):
        self.results.append({
            'test': test_name,
            'success': success,
            'message': message,
            'details': details,
            'timestamp': datetime.now().isoformat()
        })
        
    def print_summary(self):
        print("\n" + "="*80)
        print("BACKEND API TEST RESULTS SUMMARY")
        print("="*80)
        
        passed = sum(1 for r in self.results if r['success'])
        total = len(self.results)
        
        print(f"Total Tests: {total}")
        print(f"Passed: {passed}")
        print(f"Failed: {total - passed}")
        print(f"Success Rate: {(passed/total)*100:.1f}%")
        
        print("\nDETAILED RESULTS:")
        print("-" * 80)
        
        for result in self.results:
            status = "✅ PASS" if result['success'] else "❌ FAIL"
            print(f"{status} | {result['test']}")
            print(f"     Message: {result['message']}")
            if result['details']:
                print(f"     Details: {result['details']}")
            print()

async def test_campaign_stats(session, results):
    """Test GET /api/donations/stats endpoint"""
    test_name = "Campaign Stats API"
    
    try:
        url = f"{API_BASE}/donations/stats"
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                
                # Verify expected structure and values
                expected_fields = ['goal', 'current_amount', 'donor_count', 'percent_complete']
                missing_fields = [field for field in expected_fields if field not in data]
                
                if missing_fields:
                    results.add_result(test_name, False, 
                                     f"Missing fields: {missing_fields}", data)
                    return
                
                # Check expected values
                if (data['goal'] == 18500 and 
                    data['current_amount'] == 12000 and 
                    data['donor_count'] == 187 and 
                    abs(data['percent_complete'] - 64.9) < 0.1):
                    results.add_result(test_name, True, 
                                     "Campaign stats returned correct values", data)
                else:
                    results.add_result(test_name, False, 
                                     "Campaign stats values don't match expected", data)
            else:
                error_text = await response.text()
                results.add_result(test_name, False, 
                                 f"HTTP {response.status}: {error_text}")
                
    except Exception as e:
        results.add_result(test_name, False, f"Exception: {str(e)}")

async def test_stripe_create_session(session, results):
    """Test POST /api/donations/stripe/create-session endpoint"""
    test_name = "Stripe Create Session API"
    
    try:
        url = f"{API_BASE}/donations/stripe/create-session"
        payload = {
            "amount": 50.00,
            "tier_id": "tier2"
        }
        
        async with session.post(url, json=payload) as response:
            if response.status == 200:
                data = await response.json()
                
                # Verify response structure
                if 'url' in data and 'session_id' in data:
                    # Store session_id for later tests
                    results.session_id = data['session_id']
                    
                    # Verify URL format (should be Stripe checkout URL)
                    if 'checkout.stripe.com' in data['url'] or 'stripe' in data['url'].lower():
                        results.add_result(test_name, True, 
                                         "Stripe session created successfully", 
                                         f"Session ID: {data['session_id']}")
                    else:
                        results.add_result(test_name, False, 
                                         "Invalid Stripe URL format", data)
                else:
                    results.add_result(test_name, False, 
                                     "Missing required fields in response", data)
            else:
                error_text = await response.text()
                results.add_result(test_name, False, 
                                 f"HTTP {response.status}: {error_text}")
                
    except Exception as e:
        results.add_result(test_name, False, f"Exception: {str(e)}")

async def test_stripe_payment_status(session, results):
    """Test GET /api/donations/stripe/status/:sessionId endpoint"""
    test_name = "Stripe Payment Status API"
    
    if not results.session_id:
        results.add_result(test_name, False, 
                         "No session_id available from previous test")
        return
    
    try:
        url = f"{API_BASE}/donations/stripe/status/{results.session_id}"
        
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                
                # Verify response structure
                expected_fields = ['status', 'payment_status', 'amount', 'currency']
                missing_fields = [field for field in expected_fields if field not in data]
                
                if missing_fields:
                    results.add_result(test_name, False, 
                                     f"Missing fields: {missing_fields}", data)
                else:
                    # For test session, expect 'open' status and 'unpaid' payment_status
                    results.add_result(test_name, True, 
                                     "Payment status retrieved successfully", data)
            else:
                error_text = await response.text()
                results.add_result(test_name, False, 
                                 f"HTTP {response.status}: {error_text}")
                
    except Exception as e:
        results.add_result(test_name, False, f"Exception: {str(e)}")

async def test_recent_donations(session, results):
    """Test GET /api/donations/recent endpoint"""
    test_name = "Recent Donations API"
    
    try:
        url = f"{API_BASE}/donations/recent"
        
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                
                # Should return a list (may be empty initially)
                if isinstance(data, list):
                    if len(data) == 0:
                        results.add_result(test_name, True, 
                                         "Recent donations endpoint working (empty list)", 
                                         f"Returned {len(data)} donations")
                    else:
                        # Verify structure of first donation
                        first_donation = data[0]
                        expected_fields = ['name', 'amount', 'time']
                        missing_fields = [field for field in expected_fields 
                                        if field not in first_donation]
                        
                        if missing_fields:
                            results.add_result(test_name, False, 
                                             f"Missing fields in donation: {missing_fields}", 
                                             first_donation)
                        else:
                            results.add_result(test_name, True, 
                                             f"Recent donations retrieved successfully", 
                                             f"Returned {len(data)} donations")
                else:
                    results.add_result(test_name, False, 
                                     "Response is not a list", data)
            else:
                error_text = await response.text()
                results.add_result(test_name, False, 
                                 f"HTTP {response.status}: {error_text}")
                
    except Exception as e:
        results.add_result(test_name, False, f"Exception: {str(e)}")

async def test_api_connectivity(session, results):
    """Test basic API connectivity"""
    test_name = "API Connectivity"
    
    try:
        url = f"{API_BASE}/"
        
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                if data.get('message') == 'Hello World':
                    results.add_result(test_name, True, 
                                     "API is accessible and responding")
                else:
                    results.add_result(test_name, False, 
                                     "Unexpected response from API", data)
            else:
                error_text = await response.text()
                results.add_result(test_name, False, 
                                 f"HTTP {response.status}: {error_text}")
                
    except Exception as e:
        results.add_result(test_name, False, f"Exception: {str(e)}")

async def verify_pending_donation_record(session, results):
    """Verify that a pending donation record was created in MongoDB"""
    test_name = "Pending Donation Record Verification"
    
    if not results.session_id:
        results.add_result(test_name, False, 
                         "No session_id available to verify donation record")
        return
    
    # This is an indirect test - we'll check if the status endpoint 
    # can find the donation record (which implies it was created)
    try:
        url = f"{API_BASE}/donations/stripe/status/{results.session_id}"
        
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                # If we get a valid response, the donation record exists
                results.add_result(test_name, True, 
                                 "Pending donation record exists in database", 
                                 f"Amount: ${data.get('amount', 'unknown')}")
            else:
                results.add_result(test_name, False, 
                                 "Could not verify donation record existence")
                
    except Exception as e:
        results.add_result(test_name, False, f"Exception: {str(e)}")

async def run_all_tests():
    """Run all backend API tests"""
    print(f"Starting Backend API Tests...")
    print(f"Backend URL: {BACKEND_URL}")
    print(f"API Base: {API_BASE}")
    print("="*80)
    
    results = TestResults()
    
    # Create HTTP session with timeout
    timeout = aiohttp.ClientTimeout(total=30)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        
        # Test 1: Basic API connectivity
        print("Testing API connectivity...")
        await test_api_connectivity(session, results)
        
        # Test 2: Campaign stats
        print("Testing campaign stats API...")
        await test_campaign_stats(session, results)
        
        # Test 3: Stripe create session
        print("Testing Stripe create session API...")
        await test_stripe_create_session(session, results)
        
        # Test 4: Verify pending donation record
        print("Verifying pending donation record...")
        await verify_pending_donation_record(session, results)
        
        # Test 5: Stripe payment status
        print("Testing Stripe payment status API...")
        await test_stripe_payment_status(session, results)
        
        # Test 6: Recent donations
        print("Testing recent donations API...")
        await test_recent_donations(session, results)
    
    # Print results
    results.print_summary()
    
    # Return results for further processing
    return results

if __name__ == "__main__":
    # Run the tests
    results = asyncio.run(run_all_tests())
    
    # Exit with error code if any tests failed
    failed_tests = [r for r in results.results if not r['success']]
    if failed_tests:
        print(f"\n❌ {len(failed_tests)} test(s) failed!")
        sys.exit(1)
    else:
        print(f"\n✅ All tests passed!")
        sys.exit(0)