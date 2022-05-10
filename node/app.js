const express = require('express');
const bodyParser = require('body-parser');
require('isomorphic-fetch');

const app = express();
app.use(bodyParser.json());

const daprPort = process.env.DAPR_HTTP_PORT || 3500;
const stateStoreName = `statestore`;
const stateUrl = `http://localhost:${daprPort}/v1.0/state/${stateStoreName}`;
const port = 3000;

app.get('/order', (_req, res) => {
    fetch(`${stateUrl}/order`)
        .then((response) => {
            if (!response.ok) {
                throw "Could not get state.";
            }

            return response.text();
        }).then((orders) => {
        res.send(orders);
    }).catch((error) => {
        console.log(error);
        res.status(500).send({message: error});
    });
});

app.post('/neworder', (req, res) => {
    const data = req.body.data;
    const orderId = data.orderId;
    console.log("Got a new order! Order ID: " + orderId);

    const state = [{
        key: "order",
        value: data
    }];

    fetch(stateUrl, {
        method: "POST",
        body: JSON.stringify(state),
        headers: {
            "Content-Type": "application/json"
        }
    }).then((response) => {
        if (!response.ok) {
            throw "Failed to persist state.";
        }

        console.log("Successfully persisted state.");
        res.status(200).send();
    }).catch((error) => {
        console.log(error);
        res.status(500).send({message: error});
    });
});

// subscribe to the topic
app.post('/dsstatus', (req, res) => {
    // const data = req.body.data;
    console.log("PubSub received a message!");
    res.sendStatus(200);
});

// binding cron
const bindingName = "binding-cron";
const bindingUrl = `http://localhost:${daprPort}/v1.0/bindings/${bindingName}`;
let count = 0;
app.post('/binding-cron', (req, res) => {
    console.log("scheduled endpoint called ...")
    res.sendStatus(200);
    count++;
    if (count === 3) {
        console.log("scheduled endpoint called 3 times ...")
        const data = {
            'operation': 'delete'
        }
        fetch(bindingUrl, {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json"
            }
        }).then((response) => {
            if (!response.ok) {
                throw "Failed to remove cron.";
            }

            console.log("Successfully remove cron.");
            res.status(200).send();
        }).catch((error) => {
            console.log(error);
            res.status(500).send({message: error});
        });
    }
});

app.listen(port, () => console.log(`Node App listening on port ${port}!`));