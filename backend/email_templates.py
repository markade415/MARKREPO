"""
Email Templates for RocketShip Fundraising Campaign
Ade's Global Foundation Inc
"""

def get_donor_thank_you_email(donor_name, amount, tier_name=None):
    """
    Thank you email sent to donors after successful donation
    
    Args:
        donor_name: Name of the donor (e.g., "Sarah M." or "Anonymous")
        amount: Donation amount (e.g., 50.00)
        tier_name: Tier name if applicable (e.g., "Two Children")
    """
    
    tier_message = ""
    if tier_name:
        tier_message = f"""
<p style="background: #FFF1F2; border-left: 4px solid #F43F5E; padding: 15px; margin: 20px 0;">
    <strong>Your {tier_name} donation will make a direct impact!</strong>
</p>
"""
    
    email_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f9fafb;">
    <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #f9fafb; padding: 20px;">
        <tr>
            <td align="center">
                <table width="600" cellpadding="0" cellspacing="0" style="background-color: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    
                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #F43F5E 0%, #14B8A6 100%); padding: 40px 30px; text-align: center;">
                            <h1 style="color: #ffffff; margin: 0; font-size: 32px; font-weight: bold;">
                                🚀 Thank You for Your Generosity!
                            </h1>
                        </td>
                    </tr>
                    
                    <!-- Main Content -->
                    <tr>
                        <td style="padding: 40px 30px;">
                            <p style="font-size: 18px; color: #1f2937; margin: 0 0 20px 0;">
                                Dear {donor_name},
                            </p>
                            
                            <p style="font-size: 16px; color: #4b5563; line-height: 1.6; margin: 0 0 20px 0;">
                                On behalf of everyone at <strong>Ade's Global Foundation Inc</strong> and the children at 
                                <strong>RocketShip Mosaic Elementary</strong>, we want to express our heartfelt gratitude 
                                for your generous donation of <strong style="color: #F43F5E; font-size: 24px;">${amount:.2f}</strong>.
                            </p>
                            
                            {tier_message}
                            
                            <p style="font-size: 16px; color: #4b5563; line-height: 1.6; margin: 0 0 20px 0;">
                                <strong>Your gift is truly the rocket fuel that helps these little learners soar higher.</strong>
                            </p>
                            
                            <!-- Impact Box -->
                            <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #FFF7ED; border-radius: 8px; padding: 20px; margin: 20px 0;">
                                <tr>
                                    <td>
                                        <h3 style="color: #F43F5E; margin: 0 0 15px 0; font-size: 20px;">Your Impact:</h3>
                                        <ul style="color: #4b5563; line-height: 1.8; margin: 0; padding-left: 20px;">
                                            <li>Provides warm winter jackets to homeless children</li>
                                            <li>Delivers essential school supplies and books</li>
                                            <li>Brings joy through toys and treats</li>
                                            <li>Supports 300 kindergarteners (ages 3-7)</li>
                                        </ul>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="font-size: 16px; color: #4b5563; line-height: 1.6; margin: 20px 0;">
                                At RocketShip Mosaic Elementary, 60% of our 500 students are experiencing homelessness. 
                                Yet their spirits remain bright, their dreams remain big, and with your help, their futures 
                                remain full of hope.
                            </p>
                            
                            <p style="font-size: 16px; color: #4b5563; line-height: 1.6; margin: 20px 0;">
                                We are committed to fostering a supportive environment that empowers resilient youth to 
                                thrive and realize their full potential. Your generosity makes this mission possible.
                            </p>
                            
                            <!-- CTA Button -->
                            <table width="100%" cellpadding="0" cellspacing="0" style="margin: 30px 0;">
                                <tr>
                                    <td align="center">
                                        <a href="https://schooldonation.com" style="display: inline-block; background: linear-gradient(135deg, #F43F5E 0%, #14B8A6 100%); color: #ffffff; text-decoration: none; padding: 15px 40px; border-radius: 8px; font-weight: bold; font-size: 16px;">
                                            Share This Campaign
                                        </a>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="font-size: 16px; color: #4b5563; line-height: 1.6; margin: 20px 0;">
                                With deepest gratitude,
                            </p>
                            
                            <p style="font-size: 16px; color: #1f2937; font-weight: bold; margin: 0;">
                                The Ade's Global Foundation Inc Team<br>
                                <span style="color: #F43F5E;">RocketShip Mission</span>
                            </p>
                        </td>
                    </tr>
                    
                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #1f2937; padding: 30px; text-align: center;">
                            <p style="color: #9ca3af; font-size: 14px; margin: 0 0 15px 0;">
                                <strong>Ade's Global Foundation Inc</strong><br>
                                2323 Broad Way, Oakland, CA 94612
                            </p>
                            <p style="color: #9ca3af; font-size: 14px; margin: 0 0 15px 0;">
                                📧 customerservice@adesglobal-nonprofit.com<br>
                                📞 +888 681 9001 | 💬 Text: 415-926-9926
                            </p>
                            <p style="color: #6b7280; font-size: 12px; margin: 15px 0 0 0;">
                                Tax ID: [Your EIN] | 501(c)(3) Nonprofit Organization<br>
                                Your donation is tax-deductible to the extent allowed by law.
                            </p>
                        </td>
                    </tr>
                    
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
"""
    
    email_text = f"""
Dear {donor_name},

Thank you for your generous donation of ${amount:.2f} to Ade's Global Foundation Inc!

Your gift is truly the rocket fuel that helps these little learners at RocketShip Mosaic Elementary soar higher.

YOUR IMPACT:
• Provides warm winter jackets to homeless children
• Delivers essential school supplies and books
• Brings joy through toys and treats
• Supports 300 kindergarteners (ages 3-7)

At RocketShip Mosaic Elementary, 60% of our 500 students are experiencing homelessness. Your generosity helps us ensure no child faces the cold or hardship alone.

With deepest gratitude,
The Ade's Global Foundation Inc Team
RocketShip Mission

---
Ade's Global Foundation Inc
2323 Broad Way, Oakland, CA 94612
customerservice@adesglobal-nonprofit.com
Phone: +888 681 9001 | Text: 415-926-9926
"""
    
    return {
        "subject": f"Thank You for Your ${amount:.2f} Donation - RocketShip Mission",
        "html": email_html,
        "text": email_text
    }


def get_campaign_announcement_email():
    """
    Campaign announcement email to send to supporters
    """
    
    email_html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f9fafb;">
    <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #f9fafb; padding: 20px;">
        <tr>
            <td align="center">
                <table width="600" cellpadding="0" cellspacing="0" style="background-color: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    
                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #F43F5E 0%, #14B8A6 100%); padding: 40px 30px; text-align: center;">
                            <h1 style="color: #ffffff; margin: 0; font-size: 36px; font-weight: bold;">
                                🚀 We Inspire Young Learners<br>to Soar Higher
                            </h1>
                        </td>
                    </tr>
                    
                    <!-- Hero Image -->
                    <tr>
                        <td style="padding: 0;">
                            <img src="https://images.unsplash.com/photo-1588072432836-e10032774350" alt="Children learning" style="width: 100%; height: auto; display: block;">
                        </td>
                    </tr>
                    
                    <!-- Main Content -->
                    <tr>
                        <td style="padding: 40px 30px;">
                            <h2 style="color: #F43F5E; font-size: 28px; margin: 0 0 20px 0;">
                                Urgent Appeal: 300 Homeless Children Need Your Help
                            </h2>
                            
                            <p style="font-size: 18px; color: #4b5563; line-height: 1.6; margin: 0 0 20px 0;">
                                <strong>60% of students at RocketShip Mosaic Elementary are experiencing homelessness.</strong>
                            </p>
                            
                            <p style="font-size: 16px; color: #4b5563; line-height: 1.6; margin: 0 0 20px 0;">
                                These kindergarteners (ages 3-7) face cold winter days without proper jackets, 
                                limited access to books and school supplies, and uncertainty about their next meal. 
                                Yet their spirits remain bright and their dreams remain big.
                            </p>
                            
                            <!-- Impact Stats -->
                            <table width="100%" cellpadding="0" cellspacing="0" style="margin: 30px 0;">
                                <tr>
                                    <td width="50%" style="padding: 20px; background-color: #FFF1F2; border-radius: 8px; text-align: center;" valign="top">
                                        <h3 style="color: #F43F5E; font-size: 48px; margin: 0; font-weight: bold;">$25</h3>
                                        <p style="color: #4b5563; margin: 10px 0 0 0;">Warm jacket + book<br>for one child</p>
                                    </td>
                                    <td width="50%" style="padding: 20px; background-color: #ECFDF5; border-radius: 8px; text-align: center;" valign="top">
                                        <h3 style="color: #14B8A6; font-size: 48px; margin: 0; font-weight: bold;">$250</h3>
                                        <p style="color: #4b5563; margin: 10px 0 0 0;">Equips entire classroom<br>with essentials</p>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="font-size: 16px; color: #4b5563; line-height: 1.6; margin: 20px 0;">
                                Through our <strong>RocketShip Donation Event</strong>, we're delivering:
                            </p>
                            
                            <ul style="color: #4b5563; line-height: 1.8; font-size: 16px;">
                                <li>Warm winter jackets and socks</li>
                                <li>Books and school supplies</li>
                                <li>Educational toys</li>
                                <li>Candies and treats</li>
                                <li>Christmas gifts and joy</li>
                            </ul>
                            
                            <p style="font-size: 18px; color: #F43F5E; font-weight: bold; line-height: 1.6; margin: 30px 0; text-align: center;">
                                Your gift is the rocket fuel that helps these little learners soar toward brighter futures.
                            </p>
                            
                            <!-- CTA Button -->
                            <table width="100%" cellpadding="0" cellspacing="0" style="margin: 30px 0;">
                                <tr>
                                    <td align="center">
                                        <a href="https://schooldonation.com" style="display: inline-block; background: linear-gradient(135deg, #F43F5E 0%, #14B8A6 100%); color: #ffffff; text-decoration: none; padding: 20px 50px; border-radius: 8px; font-weight: bold; font-size: 20px;">
                                            Fuel the Rocket Ship Mission →
                                        </a>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="font-size: 14px; color: #6b7280; text-align: center; margin: 20px 0 0 0;">
                                Every donation makes a difference. One child, one smile, one future at a time.
                            </p>
                        </td>
                    </tr>
                    
                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #1f2937; padding: 30px; text-align: center;">
                            <p style="color: #9ca3af; font-size: 14px; margin: 0 0 15px 0;">
                                <strong>Ade's Global Foundation Inc</strong><br>
                                2323 Broad Way, Oakland, CA 94612
                            </p>
                            <p style="color: #9ca3af; font-size: 14px; margin: 0;">
                                📧 customerservice@adesglobal-nonprofit.com | 📞 +888 681 9001
                            </p>
                        </td>
                    </tr>
                    
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
"""
    
    email_text = """
🚀 WE INSPIRE YOUNG LEARNERS TO SOAR HIGHER

URGENT APPEAL: 300 Homeless Children Need Your Help

60% of students at RocketShip Mosaic Elementary are experiencing homelessness.

These kindergarteners (ages 3-7) face cold winter days without proper jackets, limited access to books and school supplies, and uncertainty about their next meal. Yet their spirits remain bright and their dreams remain big.

YOUR IMPACT:
$25 - Warm jacket + book for one child
$50 - Jackets, socks, and toys for two children
$100 - Brings warmth, books, and joy to four children
$250 - Equips entire classroom with essentials

Through our RocketShip Donation Event, we're delivering:
• Warm winter jackets and socks
• Books and school supplies
• Educational toys
• Candies and treats
• Christmas gifts and joy

Your gift is the rocket fuel that helps these little learners soar toward brighter futures.

DONATE NOW: https://schooldonation.com

Every donation makes a difference. One child, one smile, one future at a time.

---
Ade's Global Foundation Inc
2323 Broad Way, Oakland, CA 94612
customerservice@adesglobal-nonprofit.com
Phone: +888 681 9001 | Text: 415-926-9926
"""
    
    return {
        "subject": "🚀 Help 300 Homeless Children at RocketShip Elementary",
        "html": email_html,
        "text": email_text
    }


def get_campaign_update_email(current_amount, goal, donor_count, percent_complete):
    """
    Campaign progress update email
    """
    
    email_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f9fafb;">
    <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #f9fafb; padding: 20px;">
        <tr>
            <td align="center">
                <table width="600" cellpadding="0" cellspacing="0" style="background-color: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    
                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #F43F5E 0%, #14B8A6 100%); padding: 40px 30px; text-align: center;">
                            <h1 style="color: #ffffff; margin: 0; font-size: 32px; font-weight: bold;">
                                🎉 Amazing Progress Update!
                            </h1>
                        </td>
                    </tr>
                    
                    <!-- Main Content -->
                    <tr>
                        <td style="padding: 40px 30px;">
                            <p style="font-size: 18px; color: #1f2937; margin: 0 0 20px 0;">
                                Dear Supporter,
                            </p>
                            
                            <p style="font-size: 16px; color: #4b5563; line-height: 1.6; margin: 0 0 30px 0;">
                                Thanks to generous donors like you, we're making incredible progress toward our 
                                RocketShip Mission goal!
                            </p>
                            
                            <!-- Progress Stats -->
                            <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #FFF1F2; border-radius: 12px; padding: 30px; margin: 20px 0;">
                                <tr>
                                    <td align="center">
                                        <h2 style="color: #F43F5E; font-size: 48px; margin: 0; font-weight: bold;">
                                            ${current_amount:,.0f}
                                        </h2>
                                        <p style="color: #4b5563; font-size: 16px; margin: 10px 0;">
                                            raised of ${goal:,.0f} goal
                                        </p>
                                        
                                        <!-- Progress Bar -->
                                        <div style="background-color: #FFF; border-radius: 10px; height: 20px; margin: 20px 0; overflow: hidden;">
                                            <div style="background: linear-gradient(135deg, #F43F5E 0%, #14B8A6 100%); height: 100%; width: {percent_complete}%; border-radius: 10px;"></div>
                                        </div>
                                        
                                        <p style="color: #F43F5E; font-size: 32px; font-weight: bold; margin: 10px 0;">
                                            {percent_complete}%
                                        </p>
                                        <p style="color: #4b5563; font-size: 16px; margin: 0;">
                                            {donor_count} generous donors
                                        </p>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="font-size: 16px; color: #4b5563; line-height: 1.6; margin: 20px 0;">
                                Every dollar brings us closer to providing warm jackets, school supplies, and hope 
                                to 300 homeless kindergarteners at RocketShip Mosaic Elementary.
                            </p>
                            
                            <p style="font-size: 16px; color: #4b5563; line-height: 1.6; margin: 20px 0;">
                                <strong>Can you help us reach our goal?</strong> Share this campaign with friends, 
                                family, and colleagues who believe every child deserves warmth and opportunity.
                            </p>
                            
                            <!-- CTA Buttons -->
                            <table width="100%" cellpadding="0" cellspacing="0" style="margin: 30px 0;">
                                <tr>
                                    <td align="center">
                                        <a href="https://schooldonation.com" style="display: inline-block; background: linear-gradient(135deg, #F43F5E 0%, #14B8A6 100%); color: #ffffff; text-decoration: none; padding: 15px 40px; border-radius: 8px; font-weight: bold; font-size: 16px; margin: 10px;">
                                            Donate Again
                                        </a>
                                        <a href="https://schooldonation.com" style="display: inline-block; background: #ffffff; color: #F43F5E; text-decoration: none; padding: 15px 40px; border-radius: 8px; font-weight: bold; font-size: 16px; border: 2px solid #F43F5E; margin: 10px;">
                                            Share Campaign
                                        </a>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="font-size: 16px; color: #4b5563; line-height: 1.6; margin: 20px 0;">
                                Thank you for being part of this mission!
                            </p>
                            
                            <p style="font-size: 16px; color: #1f2937; font-weight: bold; margin: 20px 0 0 0;">
                                With gratitude,<br>
                                The Ade's Global Foundation Inc Team
                            </p>
                        </td>
                    </tr>
                    
                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #1f2937; padding: 30px; text-align: center;">
                            <p style="color: #9ca3af; font-size: 14px; margin: 0;">
                                Ade's Global Foundation Inc | 2323 Broad Way, Oakland, CA 94612<br>
                                customerservice@adesglobal-nonprofit.com | +888 681 9001
                            </p>
                        </td>
                    </tr>
                    
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
"""
    
    email_text = f"""
🎉 AMAZING PROGRESS UPDATE!

Dear Supporter,

Thanks to generous donors like you, we're making incredible progress toward our RocketShip Mission goal!

CURRENT PROGRESS:
${current_amount:,.0f} raised of ${goal:,.0f} goal
{percent_complete}% complete
{donor_count} generous donors

Every dollar brings us closer to providing warm jackets, school supplies, and hope to 300 homeless kindergarteners at RocketShip Mosaic Elementary.

Can you help us reach our goal? Share this campaign with friends, family, and colleagues who believe every child deserves warmth and opportunity.

DONATE OR SHARE: https://schooldonation.com

Thank you for being part of this mission!

With gratitude,
The Ade's Global Foundation Inc Team

---
Ade's Global Foundation Inc
2323 Broad Way, Oakland, CA 94612
customerservice@adesglobal-nonprofit.com
Phone: +888 681 9001
"""
    
    return {
        "subject": f"🎉 We're {percent_complete}% to our Goal - RocketShip Mission",
        "html": email_html,
        "text": email_text
    }
