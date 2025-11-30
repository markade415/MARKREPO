# Email Campaign Guide - RocketShip Fundraising

## 🎯 Overview

Your landing page now has **3 payment options**:
1. ✅ **Stripe** - Credit/debit cards (already configured with test key)
2. ✅ **Zeffy** - 100% free for nonprofits (your link integrated)
3. ⏳ **PayPal** - Coming soon

Email system is **ready to configure** when you provide Gmail credentials.

---

## 📧 EMAIL TEMPLATES AVAILABLE

### 1. **Thank You Email** (For Donors)
**When:** Automatically sent after donation
**Content:**
- Personalized greeting
- Donation amount confirmation
- Impact description
- Tax receipt information
- Share campaign CTA

### 2. **Campaign Announcement Email**
**When:** Launch campaign or recruit new supporters
**Content:**
- Emotional appeal with statistics
- Donation tier options
- Call to action button
- School and foundation information

### 3. **Progress Update Email**
**When:** Weekly or at milestones (25%, 50%, 75%)
**Content:**
- Current fundraising progress
- Visual progress bar
- Donor count
- Urgent call to action
- Share campaign CTA

---

## ⚙️ SETUP INSTRUCTIONS

### **Step 1: Create Gmail App Password**

1. **Enable 2-Step Verification:**
   - Go to: https://myaccount.google.com/security
   - Enable "2-Step Verification" if not already on

2. **Generate App Password:**
   - Go to: https://myaccount.google.com/apppasswords
   - Select: "Mail" and "Other (Custom name)"
   - Name it: "RocketShip Donations"
   - Click **"Generate"**
   - Copy the **16-character password** (looks like: `abcd efgh ijkl mnop`)

### **Step 2: Configure Email Settings**

Edit the file `/app/backend/.env` and add:

```bash
# Email Configuration
GMAIL_EMAIL=your-email@gmail.com
GMAIL_APP_PASSWORD=abcd efgh ijkl mnop
SENDER_NAME=Ade's Global Foundation Inc
```

**Replace:**
- `your-email@gmail.com` with your actual Gmail
- `abcd efgh ijkl mnop` with your 16-char app password

### **Step 3: Test Email System**

```bash
cd /app/backend
python email_sender.py
```

Should show:
```
✅ Gmail configured: your-email@gmail.com
✅ Sender name: Ade's Global Foundation Inc
Ready to send emails!
```

### **Step 4: Send Test Email**

```bash
cd /app/backend
python -c "from email_sender import send_test_email; print(send_test_email('your-test@email.com'))"
```

Check your inbox for the test email!

---

## 📨 SENDING CAMPAIGN EMAILS

### **Option 1: Campaign Announcement**

Send to multiple recipients:
```bash
python /app/send_campaign_email.py friend1@email.com friend2@email.com friend3@email.com
```

Or use an email list file (one email per line):
```bash
python /app/send_campaign_email.py --file /app/email_list.txt
```

**Email list format** (`email_list.txt`):
```
john@example.com
sarah@example.com
donor1@gmail.com
supporter@nonprofit.org
```

### **Option 2: Progress Update**

```bash
python /app/send_progress_update.py friend1@email.com friend2@email.com
```

Or with file:
```bash
python /app/send_progress_update.py --file /app/email_list.txt
```

This automatically includes current campaign statistics!

---

## 🤖 AUTOMATIC THANK YOU EMAILS (Future Setup)

**When you're ready to enable automatic emails after donations:**

1. The backend is already prepared with email templates
2. Just need to uncomment the email sending code in `/app/backend/routes/donations.py`
3. After Stripe payment completes → automatic thank you email sent
4. Includes donor name, amount, and impact statement

**Tell me when you want to activate this feature!**

---

## 📊 EMAIL ANALYTICS

### Track Email Campaign Performance:

**Gmail Method:**
- Use Gmail's "Sent" folder
- Check for replies
- Monitor bounce-backs

**Advanced (Future):**
- Add tracking pixels to measure open rates
- Use link tracking for click-through rates
- Consider SendGrid for better analytics

---

## 🎨 EMAIL TEMPLATE CUSTOMIZATION

All templates are in: `/app/backend/email_templates.py`

**To customize:**
1. Edit the template functions
2. Change text, colors, images
3. Add your logo (replace image URLs)
4. Modify call-to-action buttons

**Example changes:**
- Add your organization logo
- Change color scheme (currently rose & teal)
- Update footer text
- Add social media links

---

## 📋 SAMPLE EMAIL CAMPAIGNS

### **Campaign Launch Schedule:**

**Week 1: Announcement**
```bash
python /app/send_campaign_email.py --file all_contacts.txt
```

**Week 2: Progress Update (if 25% reached)**
```bash
python /app/send_progress_update.py --file all_contacts.txt
```

**Week 3: Urgent Appeal (if goal not met)**
```bash
python /app/send_campaign_email.py --file potential_donors.txt
```

**Week 4: Final Push**
```bash
python /app/send_progress_update.py --file all_contacts.txt
```

**After Goal Reached: Thank You to All**
```bash
# Edit template to create celebration email
python /app/send_campaign_email.py --file all_contacts.txt
```

---

## 🔒 SECURITY & PRIVACY

### **Best Practices:**

✅ **DO:**
- Keep app password secret (never share publicly)
- Store in `.env` file only
- Use Gmail App Password (not main password)
- Send to confirmed contacts only
- Include unsubscribe option (add to templates)
- Respect CAN-SPAM Act compliance

❌ **DON'T:**
- Share Gmail credentials
- Send unsolicited bulk emails
- Put passwords in code files
- Email without permission

### **Gmail Sending Limits:**
- **500 emails per day** (free Gmail account)
- **2,000 emails per day** (Google Workspace)
- Spread large campaigns over multiple days

---

## 💡 PRO TIPS

### **Building Your Email List:**

1. **From Website:**
   - Add newsletter signup form
   - Collect emails at donation confirmation
   - Create a "Stay Updated" section

2. **From Events:**
   - Collect at donation events
   - Add QR code signup sheets
   - Use tablet/iPad for instant signups

3. **From Social Media:**
   - Add "Email signup" link in bio
   - Create Facebook lead ads
   - Run Instagram stories with swipe-up

### **Increasing Open Rates:**

- **Subject lines:** Use emojis (🚀, ❤️, 🎉)
- **Send timing:** Tuesday-Thursday, 10 AM - 2 PM
- **Personalization:** Use first names when available
- **Mobile-friendly:** All templates are responsive
- **Follow-up:** Send 2-3 times during campaign

---

## 📞 SUPPORT

**If emails aren't sending:**

1. Check Gmail credentials in `.env`
2. Verify app password (16 characters, no spaces)
3. Test with single email first
4. Check Gmail "Sent" folder
5. Look for error messages

**Common errors:**
- `Authentication failed` → Wrong email or password
- `Connection refused` → Check internet connection
- `Rate limit exceeded` → Sent too many emails (wait 24 hours)

---

## ✅ QUICK START CHECKLIST

- [ ] Create Gmail App Password
- [ ] Add credentials to `/app/backend/.env`
- [ ] Run `python /app/backend/email_sender.py` to verify
- [ ] Send test email to yourself
- [ ] Create email list file (one email per line)
- [ ] Send campaign announcement
- [ ] Monitor donations and send thank-yous
- [ ] Send progress updates weekly
- [ ] Celebrate when goal is reached!

---

## 🎯 NEXT STEPS

**When ready to go live with automatic emails:**
1. Provide Gmail credentials
2. I'll enable automatic thank-you emails
3. Every donation triggers immediate email
4. Donor receives confirmation within seconds

**For now:**
- Use manual email scripts
- Send campaign announcements
- Share progress updates
- Build your email list

---

**Questions? Need help? Just ask!**

Ade's Global Foundation Inc
customerservice@adesglobal-nonprofit.com
Phone: +888 681 9001 | Text: 415-926-9926
