import {initializeApp} from "https://www.gstatic.com/firebasejs/9.14.0/firebase-app.js";
import {getDatabase, ref, child, get, set} from "https://www.gstatic.com/firebasejs/9.14.0/firebase-database.js";

function initDB(){
    const firebaseConfig = {
        apiKey: "AIzaSyBWn6HM7DSLfYc8_FYws8HdM7qPp0ysYb4",
        authDomain: "projeto-di-76003.firebaseapp.com",
        databaseURL: "https://projeto-di-76003-default-rtdb.europe-west1.firebasedatabase.app",
        projectId: "projeto-di-76003",
        storageBucket: "projeto-di-76003.appspot.com",
        messagingSenderId: "481206404599",
        appId: "1:481206404599:web:cc28bcc576208264fd1af2"
    };
    
    // Initialize Firebase
    initializeApp(firebaseConfig);
}

function writeData(userId, Humidade, Temperatura) {
    const db = getDatabase();
    set(ref(db, 'Samples/' + userId), {
        Humidade: Humidade,
        Temperatura: Temperatura,
    });
}

function readData(userId, data){
    const db = getDatabase();
    const dbRef = ref(db);
    get(child(dbRef, `Samples/${userId}`)).then((snapshot) => {
    if (snapshot.exists()) {
        data.t=snapshot.val().Temperatura;
        data.h=snapshot.val().Humidade;
    } else {
        console.log("No data available");
    }
    }).catch((error) => {
        console.error(error);
    });
}

window.initDB = initDB;
window.writeData = writeData;
window.readData = readData;