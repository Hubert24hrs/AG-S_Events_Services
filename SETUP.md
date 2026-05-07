# Firebase Setup Guide — AG's Event Services

## Step-by-Step (5 minutes)

### 1. Create a Firebase Project
1. Go to https://console.firebase.google.com
2. Click **"Add project"** → name it `ags-events` → Continue
3. Disable Google Analytics (optional) → Click **"Create project"**

### 2. Enable Firestore Database
1. In the left sidebar → **Build → Firestore Database**
2. Click **"Create database"**
3. Choose **"Start in test mode"** (allows all reads/writes for 30 days)
4. Select a region (e.g., `europe-west1` for Nigeria) → **Enable**

### 3. Register Your Web App
1. In Project Overview → click the **`</>`** (Web) icon
2. App nickname: `AG Events Web` → **Register app**
3. You'll see a config object like this:

```js
const firebaseConfig = {
  apiKey: "AIza...",
  authDomain: "ags-events.firebaseapp.com",
  projectId: "ags-events",
  storageBucket: "ags-events.appspot.com",
  messagingSenderId: "123456789",
  appId: "1:123456789:web:abc123"
};
```

### 4. Paste Config into firebase-config.js
Open `firebase-config.js` and replace the placeholder values with your actual values.

### 5. Set Firestore Security Rules (Important!)
In Firestore → **Rules** tab, replace the default rules with:

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Public can submit contact form messages
    match /messages/{id} {
      allow create: if true;
      allow read, update, delete: if false;
    }
    // All other collections: public read of published items only
    match /news/{id} {
      allow read: if resource.data.published == true;
    }
    match /events/{id} {
      allow read: if resource.data.published == true;
    }
    match /testimonials/{id} {
      allow read: if resource.data.active == true;
    }
    // Admin writes — for now all writes allowed (secure with Auth later)
    match /{document=**} {
      allow write: if true;
    }
  }
}
```

Click **Publish**.

### 6. Test
1. Open `admin.html` in your browser
2. Login with password: `Agatha@agsevent202612345$`
3. Create a test news article → check if it appears in the News tab

---

## Admin Access

- **URL:** `https://hubert24hrs.github.io/AG-S_Events_Services/admin.html`
- **Password:** `Agatha@agsevent202612345$`
- To change password: edit `admin.html`, find `const ADMIN_PWD = 'Agatha@agsevent202612345$'` and update it.

---

## What Admin Can Do

| Tab | Actions |
|-----|---------|
| **Dashboard** | View stats (article count, events, messages, testimonials) |
| **News Articles** | Create, edit, delete news articles. Toggle published/draft. |
| **Events** | Add/edit/delete upcoming events shown on the site. |
| **Messages** | View contact form submissions, mark as read, delete. |
| **Testimonials** | Manage client testimonials shown on site. |

---

## How the Site Reads Admin Content

After Firebase is configured, the main `index.html` will:
- Load **News** from `/news` collection (published only) instead of mock data
- Load **Events** from `/events` collection instead of hardcoded list  
- Save **Contact form** submissions to `/messages` collection automatically

---

## Upgrading Security (Optional)
The current setup uses a simple password. For production, enable **Firebase Authentication**:
1. Firebase Console → Build → Authentication → Sign-in method
2. Enable **Email/Password**
3. Replace the password check in `admin.html` with Firebase Auth sign-in
