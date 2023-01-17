import {initializeApp} from "https://www.gstatic.com/firebasejs/9.14.0/firebase-app.js";
import {getDatabase, ref, child, get, set} from "https://www.gstatic.com/firebasejs/9.14.0/firebase-database.js";

function initDB(){
    const firebaseConfig = {
        apiKey: "...",
        authDomain: "...",
        databaseURL: "...",
        projectId: "...",
        storageBucket: "...",
        messagingSenderId: "...",
        appId: "..."
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
