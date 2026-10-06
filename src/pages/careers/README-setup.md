# Talent Application — Google Sheets Setup

## Step 1 — Create the Google Sheet

1. Go to sheets.google.com (signed in as info@avinuevents.com)
2. Create a new sheet named **"Avinu Talent Applications"**
3. Copy the sheet's URL — you'll need its ID later (the long string between `/d/` and `/edit`)

## Step 2 — Deploy the Google Apps Script

1. Open the sheet → Extensions → Apps Script
2. Delete the placeholder code and paste the script below
3. Replace `SHEET_ID` with your sheet's ID and `NOTIFY_EMAIL` if needed
4. Click **Deploy → New deployment**
   - Type: **Web app**
   - Execute as: **Me**
   - Who has access: **Anyone**
5. Click **Deploy** → authorize the app → copy the **Web app URL**

## Step 3 — Paste the URL into the Astro page

Open `src/pages/careers/index.astro` and replace the empty string:

```ts
const SCRIPT_URL = 'PASTE_YOUR_WEB_APP_URL_HERE';
```

---

## Google Apps Script Code

```javascript
const SHEET_ID   = 'YOUR_GOOGLE_SHEET_ID_HERE';
const SHEET_NAME = 'Applications';
const NOTIFY_EMAIL = 'info@avinuevents.com';

function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const ss    = SpreadsheetApp.openById(SHEET_ID);
    let sheet   = ss.getSheetByName(SHEET_NAME);

    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
      // Header row
      sheet.appendRow([
        'Timestamp', 'Name', 'Email', 'Phone', 'City',
        'Category', 'Experience', 'Languages',
        'Website', 'Demo Video', 'Bio', 'Referral'
      ]);
      sheet.getRange(1, 1, 1, 12).setFontWeight('bold');
    }

    sheet.appendRow([
      new Date().toLocaleString('en-US', { timeZone: 'America/New_York' }),
      data.name      || '',
      data.email     || '',
      data.phone     || '',
      data.city      || '',
      data.category  || '',
      data.experience|| '',
      data.languages || '',
      data.website   || '',
      data.video     || '',
      data.bio       || '',
      data.referral  || '',
    ]);

    // Email notification
    GmailApp.sendEmail(
      NOTIFY_EMAIL,
      '🎤 New Talent Application — ' + (data.name || 'Unknown'),
      [
        'A new talent application has been submitted on avinuevents.com.',
        '',
        'Name:       ' + (data.name       || '—'),
        'Email:      ' + (data.email      || '—'),
        'Phone:      ' + (data.phone      || '—'),
        'City:       ' + (data.city       || '—'),
        'Category:   ' + (data.category   || '—'),
        'Experience: ' + (data.experience || '—'),
        'Languages:  ' + (data.languages  || '—'),
        'Website:    ' + (data.website    || '—'),
        'Demo Video: ' + (data.video      || '—'),
        '',
        'Bio:',
        data.bio || '—',
        '',
        'Referral: ' + (data.referral || '—'),
        '',
        'View all applications: https://docs.google.com/spreadsheets/d/' + SHEET_ID,
      ].join('\n')
    );

    return ContentService
      .createTextOutput(JSON.stringify({ status: 'ok' }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'error', message: err.message }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
```
