#!/usr/bin/env python3
"""
Send Campaign Announcement Email

Usage:
  python send_campaign_email.py email1@example.com email2@example.com ...

Or use a file with email list (one per line):
  python send_campaign_email.py --file emails.txt
"""

import sys
import os
sys.path.insert(0, '/app/backend')

from email_sender import send_bulk_emails
from email_templates import get_campaign_announcement_email

def main():
    emails = []
    
    # Check if using file input
    if len(sys.argv) > 2 and sys.argv[1] == '--file':
        filename = sys.argv[2]
        try:
            with open(filename, 'r') as f:
                emails = [line.strip() for line in f if line.strip() and '@' in line]
        except FileNotFoundError:
            print(f"❌ File not found: {filename}")
            return
    else:
        # Use command line arguments
        emails = sys.argv[1:]
    
    if not emails:
        print("❌ No email addresses provided!")
        print("\nUsage:")
        print("  python send_campaign_email.py email1@example.com email2@example.com")
        print("  python send_campaign_email.py --file emails.txt")
        return
    
    print(f"\n📧 Sending campaign announcement to {len(emails)} recipients...")
    print("=" * 60)
    
    # Get email template
    template = get_campaign_announcement_email()
    
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
    
    # Show detailed results
    for result in results['results']:
        status = "✅" if result['success'] else "❌"
        print(f"{status} {result['email']}: {result['message']}")

if __name__ == "__main__":
    main()
