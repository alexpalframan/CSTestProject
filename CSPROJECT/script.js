// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyB7maKslK92lsBT51meQCK7bSSKT4cDme4",
  authDomain: "lc-cs-test.firebaseapp.com",
  databaseURL: "https://lc-cs-test-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "lc-cs-test",
  storageBucket: "lc-cs-test.appspot.com",
  messagingSenderId: "1096967742900",
  appId: "1:1096967742900:web:da3522497c353540bb7ee1"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);