"""
Email Sender System for RocketShip Fundraising Campaign
Ade's Global Foundation Inc

SETUP INSTRUCTIONS:
1. Enable 2-Step Verification in Gmail: https://myaccount.google.com/security
2. Create App Password: https://myaccount.google.com/apppasswords
3. Update .env file with:
   GMAIL_EMAIL=your-email@gmail.com
   GMAIL_APP_PASSWORD=your-16-char-app-password
   SENDER_NAME=Ade's Global Foundation Inc
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

# Email configuration
GMAIL_EMAIL = os.getenv('GMAIL_EMAIL', '')
GMAIL_APP_PASSWORD = os.getenv('GMAIL_APP_PASSWORD', '')
SENDER_NAME = os.getenv('SENDER_NAME', "Ade's Global Foundation Inc")

def send_email(to_email, subject, html_content, text_content):
    """
    Send an email using Gmail SMTP
    
    Args:
        to_email: Recipient email address
        subject: Email subject line
        html_content: HTML version of email
        text_content: Plain text version of email
    
    Returns:
        dict: {"success": bool, "message": str}
    """
    
    if not GMAIL_EMAIL or not GMAIL_APP_PASSWORD:
        return {
            "success": False,
            "message": "Gmail credentials not configured. Please set GMAIL_EMAIL and GMAIL_APP_PASSWORD in .env"
        }
    
    try:
        # Create message
        message = MIMEMultipart('alternative')
        message['From'] = f"{SENDER_NAME} <{GMAIL_EMAIL}>"
        message['To'] = to_email
        message['Subject'] = subject
        message['Reply-To'] = GMAIL_EMAIL
        
        # Attach both plain text and HTML versions
        part1 = MIMEText(text_content, 'plain')
        part2 = MIMEText(html_content, 'html')
        
        message.attach(part1)
        message.attach(part2)
        
        # Connect to Gmail SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(GMAIL_EMAIL, GMAIL_APP_PASSWORD)
            server.send_message(message)
        
        return {
            "success": True,
            "message": f"Email sent successfully to {to_email}"
        }
        
    except smtplib.SMTPAuthenticationError:
        return {
            "success": False,
            "message": "Gmail authentication failed. Please check your email and app password."
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"Failed to send email: {str(e)}"
        }


def send_bulk_emails(email_list, subject, html_content, text_content):
    """
    Send the same email to multiple recipients
    
    Args:
        email_list: List of email addresses
        subject: Email subject
        html_content: HTML email content
        text_content: Plain text email content
    
    Returns:
        dict: {"success_count": int, "failed_count": int, "results": list}
    """
    
    results = []
    success_count = 0
    failed_count = 0
    
    for email in email_list:
        result = send_email(email, subject, html_content, text_content)
        results.append({
            "email": email,
            "success": result["success"],
            "message": result["message"]
        })
        
        if result["success"]:
            success_count += 1
        else:
            failed_count += 1
    
    return {
        "success_count": success_count,
        "failed_count": failed_count,
        "total": len(email_list),
        "results": results
    }


# Example usage functions

def send_test_email(test_email):
    """
    Send a test email to verify configuration
    """
    subject = "Test Email - RocketShip Mission"
    html = """
    <html>
        <body>
            <h2>Test Email Successful!</h2>
            <p>Your Gmail integration is working correctly.</p>
            <p>You can now send automated thank-you emails to donors.</p>
            <br>
            <p><strong>Ade's Global Foundation Inc</strong></p>
        </body>
    </html>
    """
    text = "Test Email Successful! Your Gmail integration is working correctly."
    
    return send_email(test_email, subject, html, text)


if __name__ == "__main__":
    # Test the email system
    print("=" * 60)
    print("EMAIL SYSTEM TEST")
    print("=" * 60)
    
    if not GMAIL_EMAIL:
        print("\n❌ Gmail not configured!")
        print("\nTo set up:")
        print("1. Create Gmail App Password")
        print("2. Add to /app/backend/.env:")
        print("   GMAIL_EMAIL=your-email@gmail.com")
        print("   GMAIL_APP_PASSWORD=your-app-password")
        print("   SENDER_NAME=Ade's Global Foundation Inc")
    else:
        print(f"\n✅ Gmail configured: {GMAIL_EMAIL}")
        print(f"✅ Sender name: {SENDER_NAME}")
        print("\nReady to send emails!")
        print("\nTo send a test email, run:")
        print(f"  python -c \"from email_sender import send_test_email; print(send_test_email('test@example.com'))\"")
