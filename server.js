'use strict';

const express = require('express');
const app = express();
const bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
const {spawn} = require('child_process');
const port = 3000;

app.get('/', (req, res) => {
    let dataToSend;
    // spawn new child process to call the python script
    console.log("body : "+req.query.symbol);
    const symbol = req.query.symbol;
    if (symbol === undefined){
        return console.log("symbol is undefined")
    }
    const python = spawn('python', ['ImportAlphavantage.py',symbol]);
    // collect data from script
    python.stdout.on('data', function (data) {
        console.log('---Pipe data from python script---');
        dataToSend = data.toString();
        console.log(dataToSend);
    });
    // in close event we are sure that stream from child process is closed
    python.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        // send data to browser
        res.send(dataToSend)
    });
});
app.listen(port, () => console.log(`Example app listening on port ${port}!`));