const express = require("express");
const app = express();

const MILLIS_IN_SECOND = 1000;

const PORT = 3000;
const TIMEOUT = 5*MILLIS_IN_SECOND;

// Endpoint definition --> classic health check
app.get("/", (request, response) => {
    response.status(200).send("Ping Node.js");
});

// Force sleep --> simulate HTTP connection to other service or DB access
app.get("/timeout", (request, response) => {
    setTimeout(() => {
        response.status(200).send("Timeout Node.js");
    }, TIMEOUT);
});

// Long loop --> simulate heavy processing over data
app.get("/loop", (request, response) => {
    let start = Date.now();
    let array = [];
    let message = "Full process.";
    for (let i = 0; i < 1000; i++) {
        if (Date.now() - start > TIMEOUT) {
            message = "Time Out!";
            break;
        }
        for (let j = 0; j < i; j++) array = array.concat(j);
        let length = array.length;
        for (let k = 0; k < length; k++) console.log(array[i]);
    }
    response.status(200).send("Heavy processing Node.js - " + message);
});

// Server start up
app.listen(PORT, () => {
    // Start up function
    console.log("Listening on port 3000!");
});
