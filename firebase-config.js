// Firebase configuration for AG's Event Services
// Generated automatically on 2026-05-07
const firebaseConfig = {
  apiKey: "AIzaSyD9NoCo64wFDYMVMCqPG4-iP1VL7GHSenc",
  authDomain: "ags-events-services.firebaseapp.com",
  projectId: "ags-events-services",
  storageBucket: "ags-events-services.firebasestorage.app",
  messagingSenderId: "631997568122",
  appId: "1:631997568122:web:7aa8e64fbf6af1a59597c3",
  measurementId: "G-5P8FKZE3VP"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
window.db = firebase.firestore();
window.FIREBASE_READY = true;

console.log("Firebase initialized successfully for ags-events-services");
