/**
 * AG'S EVENT SERVICES — Firebase Configuration
 * =============================================
 * Replace the placeholder values below with your actual Firebase project config.
 * See SETUP.md for step-by-step instructions.
 *
 * Get your config from:
 *   Firebase Console → Project Settings → Your Apps → Web App → SDK setup and configuration
 */

const firebaseConfig = {
  apiKey:            "PASTE_YOUR_API_KEY_HERE",
  authDomain:        "PASTE_YOUR_AUTH_DOMAIN_HERE",
  projectId:         "PASTE_YOUR_PROJECT_ID_HERE",
  storageBucket:     "PASTE_YOUR_STORAGE_BUCKET_HERE",
  messagingSenderId: "PASTE_YOUR_MESSAGING_SENDER_ID_HERE",
  appId:             "PASTE_YOUR_APP_ID_HERE"
};

// Initialize Firebase (compat mode — works with CDN scripts)
if (typeof firebase !== 'undefined') {
  if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
  }
  window.db = firebase.firestore();
  window.FIREBASE_READY = true;
  console.log('[AG Events] Firebase connected ✓');
} else {
  window.FIREBASE_READY = false;
  console.warn('[AG Events] Firebase SDK not loaded — running in offline/demo mode.');
}
