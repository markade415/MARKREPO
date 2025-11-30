# 🚀 Complete Setup Guide - RocketShip Fundraising Campaign

## 📱 YOUR OFFICIAL LINKS

### **Primary Domain (Share This!):**
```
https://schooldonation.com
```
*(After you connect the domain in Emergent - see instructions below)*

### **Backup/Current Link:**
```
https://child-rocket-fuel.preview.emergentagent.com
```
*(Always works - use for testing)*

---

## 🎨 COLOR SCHEME

**Your landing page uses a warm, compassionate nonprofit color theme:**
- **Primary:** Rose Pink (#F43F5E) - Compassion, urgency, warmth
- **Secondary:** Teal (#14B8A6) - Trust, hope, growth
- **Professional and emotionally engaging**

---

## 💳 PAYMENT OPTIONS CONFIGURED

### ✅ **1. Stripe (Credit/Debit Cards)**
- **Status:** Configured with test key
- **Current:** `sk_test_emergent` (test mode)
- **For Production:**
  1. Create account at https://stripe.com
  2. Connect your bank account
  3. Get live API key (`sk_live_...`)
  4. Replace in `/app/backend/.env`
  5. Restart backend: `sudo supervisorctl restart backend`

### ✅ **2. Zeffy Platform**
- **Status:** Integrated and working
- **Your Link:** https://www.zeffy.com/en-US/donation-form/donate-to-make-a-difference-5481
- **Benefit:** 100% free for nonprofits (no transaction fees)
- **Opens in new tab when selected**

### ⏳ **3. PayPal**
- **Status:** Coming soon
- **Currently shows "use Stripe or Zeffy" message**

---

## 🌐 CONNECTING SCHOOLDONATION.COM

### **Step 1: Purchase Domain (If Not Done)**
1. Go to Namecheap.com or GoDaddy.com
2. Search: `schooldonation.com`
3. Purchase (~$12/year)
4. Complete checkout

### **Step 2: Connect to Emergent**
1. Log in to Emergent: https://emergent.sh
2. Go to your project: "child-rocket-fuel"
3. Click **"Link Domain"** button
4. Enter: `schooldonation.com`
5. Click **"Entri"**
6. **Follow the DNS instructions shown**

### **Step 3: Update DNS Settings**

**In your domain provider (Namecheap/GoDaddy):**
1. Go to DNS Management
2. **Delete ALL existing A records**
3. Add the DNS records shown by Emergent
4. Save changes

**Example DNS Records:**
```
Type: A
Host: @
Value: [IP from Emergent]
TTL: Automatic
```

### **Step 4: Wait for Activation**
- ⏱️ **5-15 minutes:** Usually live
- ⏱️ **Up to 24 hours:** Maximum wait
- 🔒 **SSL Certificate:** Automatically added (HTTPS)

**Test:** Visit https://schooldonation.com

---

## 📧 EMAIL SYSTEM SETUP

### **What's Ready:**
✅ Professional email templates created:
- Donor thank-you email
- Campaign announcement email  
- Progress update email

✅ Email sending scripts ready
✅ Bulk email support
✅ Beautiful HTML + plain text versions

### **What You Need to Do:**

1. **Create Gmail App Password:**
   - Go to: https://myaccount.google.com/security
   - Enable 2-Step Verification
   - Go to: https://myaccount.google.com/apppasswords
   - Create password for "RocketShip Donations"
   - Copy the 16-character password

2. **Configure Backend:**
   Edit `/app/backend/.env` and add:
   ```
   GMAIL_EMAIL=your-email@gmail.com
   GMAIL_APP_PASSWORD=your-16-char-password
   SENDER_NAME=Ade's Global Foundation Inc
   ```

3. **Test Email System:**
   ```bash
   cd /app/backend
   python email_sender.py
   ```

4. **Send Campaign Emails:**
   ```bash
   # To specific people
   python /app/send_campaign_email.py friend1@email.com friend2@email.com
   
   # From email list file
   python /app/send_campaign_email.py --file emails.txt
   ```

**See `/app/EMAIL_CAMPAIGN_GUIDE.md` for complete email instructions**

---

## 🎯 CAMPAIGN MANAGEMENT

### **View Current Stats:**
```bash
cd /app
python view_donations.py
```

Shows:
- All donations received
- Payment status (completed/pending)
- Total amounts
- Donor count

### **Update Campaign Progress:**
```bash
cd /app
python update_campaign_stats.py
```

Edit the values in the script:
- `new_goal` = Campaign goal ($18,500)
- `new_current` = Amount raised
- `new_donor_count` = Number of donors

### **Send Progress Update:**
```bash
python /app/send_progress_update.py --file emails.txt
```

Automatically includes current statistics in email!

---

## 📊 DASHBOARD ACCESS

### **1. Stripe Dashboard**
**URL:** https://dashboard.stripe.com

**What you can do:**
- View all donations
- See payment details
- Track money transfers to bank
- Download reports
- Issue refunds
- Manage disputes

**Sections:**
- **Home** → Overview
- **Payments** → All donations
- **Balance** → Available funds
- **Customers** → Donor list
- **Reports** → Export data

### **2. Zeffy Dashboard**
**URL:** https://www.zeffy.com (log in with your account)

**What you can do:**
- View Zeffy donations
- Download reports
- Manage recurring donations
- See donor information

### **3. Database (MongoDB)**
**Option A: MongoDB Compass (Desktop App)**
1. Download: https://www.mongodb.com/try/download/compass
2. Connect: `mongodb://localhost:27017`
3. Database: `test_database`
4. Collections:
   - `donations` → All donation records
   - `campaign_stats` → Progress tracking

**Option B: Command Line**
```bash
mongosh mongodb://localhost:27017
use test_database
db.donations.find().pretty()
db.campaign_stats.find().pretty()
```

---

## 🔧 MAKING CHANGES

### **Website Content Changes:**

**1. Change text/images:**
- File: `/app/frontend/src/pages/LandingPage.jsx`
- Edit content directly
- Save and hot-reload updates automatically

**2. Update donation tiers ($25, $50, $100, $250):**
- File: `/app/frontend/src/mock.js`
- Edit amounts and descriptions

**3. Change colors:**
- Current: Rose & Teal
- Files: `/app/frontend/src/pages/LandingPage.jsx` and `/app/frontend/src/components/DonationForm.jsx`
- Search/replace color classes (e.g., `rose-500` → `blue-500`)

**4. Restart services (if needed):**
```bash
sudo supervisorctl restart all
```

### **Email Template Changes:**
- File: `/app/backend/email_templates.py`
- Edit HTML and text content
- Add your logo, change colors, update text

---

## 📱 SHARING YOUR CAMPAIGN

### **1. Social Media Posts**

**Facebook/Instagram:**
```
🚀 Help us support 300 homeless children!

60% of students at RocketShip Elementary are homeless. Your donation provides warm jackets, school supplies, and hope.

Every gift matters! ❤️

Donate: https://schooldonation.com

#RocketShipMission #AdesGlobalFoundation #HelpKids
```

**Twitter:**
```
🚀 60% of RocketShip Elementary students are homeless. Help us provide warmth, books & hope to 300 kids.

Donate: https://schooldonation.com

Every gift makes a difference! ❤️
```

### **2. Email Campaign**
```bash
python /app/send_campaign_email.py --file all_contacts.txt
```

### **3. QR Code for Print Materials**
1. Go to: https://qr-code-generator.com
2. Enter: `https://schooldonation.com`
3. Download high-resolution QR code
4. Print on flyers, posters, business cards

### **4. Text Message**
```
Hi! I'm raising funds for homeless children at RocketShip Elementary. 
60% of 500 students need warm jackets & school supplies. 
Can you help? https://schooldonation.com
Every donation makes a difference! 🚀
```

---

## 🎯 LAUNCH CHECKLIST

### **Before Going Live:**

**Technical:**
- [ ] Connect schooldonation.com domain
- [ ] Switch Stripe to live API key (`sk_live_...`)
- [ ] Test a $1 donation end-to-end
- [ ] Verify money reaches your bank account
- [ ] Configure Gmail for automated emails
- [ ] Test email sending

**Content:**
- [ ] Review all text on landing page
- [ ] Verify contact information (email, phone)
- [ ] Check all links work
- [ ] Test on mobile device
- [ ] Proofread for typos

**Marketing:**
- [ ] Create email list
- [ ] Prepare social media posts
- [ ] Design QR code flyers
- [ ] Draft text messages
- [ ] Schedule launch announcement

### **Launch Day:**
- [ ] Send campaign announcement email
- [ ] Post on all social media
- [ ] Share with friends and family
- [ ] Send text messages to contacts
- [ ] Monitor first donations
- [ ] Thank early donors personally

### **Ongoing (Weekly):**
- [ ] Check campaign progress
- [ ] Send progress update emails
- [ ] Post social media updates
- [ ] Thank new donors
- [ ] Share donor testimonials
- [ ] Adjust strategy if needed

---

## 🆘 TROUBLESHOOTING

### **Website Not Loading:**
```bash
# Check if services are running
sudo supervisorctl status

# Restart if needed
sudo supervisorctl restart all

# Check logs
tail -f /var/log/supervisor/frontend.*.log
tail -f /var/log/supervisor/backend.*.log
```

### **Payments Not Working:**
1. Check Stripe API key in `/app/backend/.env`
2. Verify backend is running: `sudo supervisorctl status backend`
3. Test in browser console for errors
4. Check Stripe dashboard for webhook errors

### **Emails Not Sending:**
1. Verify Gmail credentials in `/app/backend/.env`
2. Test: `cd /app/backend && python email_sender.py`
3. Check app password (16 characters)
4. Send test email first

### **Domain Not Working:**
1. Wait 15+ minutes after DNS changes
2. Check DNS propagation: https://dnschecker.org
3. Verify DNS records in domain provider
4. Re-link domain in Emergent

---

## 📞 QUICK REFERENCE

```
═══════════════════════════════════════════════════════
           ROCKETSHIP FUNDRAISING - QUICK ACCESS
═══════════════════════════════════════════════════════

🌐 OFFICIAL LINK:
   https://schooldonation.com

🔗 BACKUP LINK:
   https://child-rocket-fuel.preview.emergentagent.com

💳 PAYMENT OPTIONS:
   • Stripe (configured)
   • Zeffy (integrated)
   • PayPal (coming soon)

💰 ZEFFY LINK:
   https://www.zeffy.com/en-US/donation-form/donate-to-make-a-difference-5481

📊 DASHBOARDS:
   • Stripe: https://dashboard.stripe.com
   • Zeffy: https://www.zeffy.com
   • MongoDB: mongodb://localhost:27017

🔧 USEFUL COMMANDS:
   View donations:     python /app/view_donations.py
   Update stats:       python /app/update_campaign_stats.py
   Send emails:        python /app/send_campaign_email.py --file emails.txt
   Restart services:   sudo supervisorctl restart all

📧 CONTACT:
   customerservice@adesglobal-nonprofit.com
   Phone: +888 681 9001
   Text: 415-926-9926

🏫 SCHOOL:
   RocketShip Mosaic Elementary
   950 Owsley Avenue, San Jose, CA 95122
═══════════════════════════════════════════════════════
```

---

## 🎉 SUCCESS!

**Your fundraising campaign is ready to launch!**

**What you have:**
✅ Beautiful, professional landing page
✅ Multiple payment options (Stripe, Zeffy)
✅ Real-time progress tracking
✅ Email campaign system ready
✅ Database for donation tracking
✅ Mobile-responsive design
✅ Secure payment processing
✅ Professional nonprofit branding

**Next steps:**
1. Connect schooldonation.com
2. Switch to live Stripe key (when ready)
3. Configure Gmail for emails
4. Launch your campaign!

**You're helping 300 homeless children at RocketShip Elementary get the warmth, education, and hope they deserve. That's incredible! 🚀❤️**

---

**Need help? Questions? Just ask!**

Ade's Global Foundation Inc
Making a difference, one child at a time.
