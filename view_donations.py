#!/usr/bin/env python3
"""
Script to view all donations
Shows complete donation history from the database
"""

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime

async def view_donations():
    # Connect to MongoDB
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["test_database"]
    
    # Get all donations
    donations = await db.donations.find().to_list(1000)
    
    if not donations:
        print("📭 No donations yet!")
        print("Donations will appear here after someone donates on your site.")
        client.close()
        return
    
    print(f"\n💰 DONATION HISTORY ({len(donations)} total)\n")
    print("=" * 80)
    
    total_completed = 0
    total_pending = 0
    
    for i, donation in enumerate(donations, 1):
        amount = donation.get('amount', 0)
        status = donation.get('payment_status', 'unknown')
        tier = donation.get('tier_id', 'custom')
        created = donation.get('created_at', datetime.now())
        session_id = donation.get('session_id', 'N/A')[:20] + "..."
        
        status_symbol = "✅" if status == "completed" else "⏳" if status == "pending" else "❌"
        
        print(f"{i}. {status_symbol} ${amount:.2f} - {status.upper()}")
        print(f"   Tier: {tier} | Session: {session_id}")
        print(f"   Date: {created}")
        print("-" * 80)
        
        if status == "completed":
            total_completed += amount
        elif status == "pending":
            total_pending += amount
    
    print(f"\n📊 SUMMARY:")
    print(f"   ✅ Completed: ${total_completed:.2f}")
    print(f"   ⏳ Pending: ${total_pending:.2f}")
    print(f"   📈 Total: ${total_completed + total_pending:.2f}")
    
    client.close()

if __name__ == "__main__":
    asyncio.run(view_donations())
