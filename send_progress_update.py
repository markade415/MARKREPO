#!/usr/bin/env python3
"""
Send Campaign Progress Update Email

Usage:
  python send_progress_update.py email1@example.com email2@example.com ...

Or use a file:
  python send_progress_update.py --file emails.txt
"""

import sys
import asyncio
sys.path.insert(0, '/app/backend')

from motor.motor_asyncio import AsyncIOMotorClient
from email_sender import send_bulk_emails
from email_templates import get_campaign_update_email

async def get_campaign_stats():
    """Fetch current campaign statistics"""
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["test_database"]
    
    stats = await db.campaign_stats.find_one({"campaign_name": "RocketShip Mission"})
    client.close()
    
    if not stats:
        return None
    
    return {
        "current_amount": stats['current_amount'],
        "goal": stats['goal'],
        "donor_count": stats['donor_count'],
        "percent_complete": stats['percent_complete']
    }

def main():
    emails = []
    
    # Parse command line arguments
    if len(sys.argv) > 2 and sys.argv[1] == '--file':
        filename = sys.argv[2]
        try:
            with open(filename, 'r') as f:
                emails = [line.strip() for line in f if line.strip() and '@' in line]
        except FileNotFoundError:
            print(f"❌ File not found: {filename}")
            return
    else:
        emails = sys.argv[1:]
    
    if not emails:
        print("❌ No email addresses provided!")
        print("\nUsage:")
        print("  python send_progress_update.py email1@example.com email2@example.com")
        print("  python send_progress_update.py --file emails.txt")
        return
    
    # Get current campaign stats
    print("\n📊 Fetching campaign statistics...")
    stats = asyncio.run(get_campaign_stats())
    
    if not stats:
        print("❌ Could not fetch campaign statistics!")
        return
    
    print(f"\nCurrent Progress:")
    print(f"  Raised: ${stats['current_amount']:,.0f} of ${stats['goal']:,.0f}")
    print(f"  Progress: {stats['percent_complete']}%")
    print(f"  Donors: {stats['donor_count']}")
    print()
    
    print(f"📧 Sending progress update to {len(emails)} recipients...")
    print("=" * 60)
    
    # Get email template with current stats
    template = get_campaign_update_email(
        stats['current_amount'],
        stats['goal'],
        stats['donor_count'],
        stats['percent_complete']
    )
    
    # Send emails
    results = send_bulk_emails(
        emails,
        template['subject'],
        template['html'],
        template['text']
    )
    
    print(f"\n✅ Successfully sent: {results['success_count']}")
    print(f"❌ Failed: {results['failed_count']}")
    print("=" * 60)
    
    for result in results['results']:
        status = "✅" if result['success'] else "❌"
        print(f"{status} {result['email']}: {result['message']}")

if __name__ == "__main__":
    main()
