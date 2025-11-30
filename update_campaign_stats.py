#!/usr/bin/env python3
"""
Script to update campaign statistics
Run this to change the goal, current amount, or donor count
"""

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def update_stats():
    # Connect to MongoDB
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["test_database"]
    
    # ===== EDIT THESE VALUES =====
    new_goal = 18500.00          # Campaign goal amount
    new_current = 10360.00       # Amount raised so far
    new_donor_count = 161        # Number of donors
    # =============================
    
    # Calculate percentage
    new_percent = round((new_current / new_goal) * 100, 1)
    
    # Update database
    result = await db.campaign_stats.update_one(
        {"campaign_name": "RocketShip Mission"},
        {
            "$set": {
                "goal": new_goal,
                "current_amount": new_current,
                "donor_count": new_donor_count,
                "percent_complete": new_percent
            }
        }
    )
    
    print(f"✅ Updated campaign stats:")
    print(f"   Goal: ${new_goal:,.2f}")
    print(f"   Raised: ${new_current:,.2f}")
    print(f"   Donors: {new_donor_count}")
    print(f"   Progress: {new_percent}%")
    
    client.close()

if __name__ == "__main__":
    asyncio.run(update_stats())
