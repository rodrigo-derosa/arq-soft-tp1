const express = require("express");
const app = express();

const MILLIS_IN_SECOND = 1000;

const PORT = 3000;
const TIMEOUT = 5*MILLIS_IN_SECOND;

// Endpoint definition
app.get("/", (request, response) => {
    response.status(200).send("Ping Node.js!");
});

// Force sleep
app.get("/timeout", (request, response) => {
    setTimeout(() => {
        response.status(200).send("Timeout Node.js")
    }, TIMEOUT);
});

// Server start up
app.listen(PORT, () => {
    // Start up function
    console.log("Listening on port 3000!");
});
