"use strict"
const PORT = 8080

const {logger} = require('./components/logger')
const express = require('express')
const bodyParser = require('body-parser')
const helmet = require('helmet')
const DDoS = require('dddos')
const app = express()
const http = require('http').Server(app)
const rain = require('./components/rain').RAIN.getInstance()
const index = require('./routes/index')
const ec = require('./routes/ec')
const {cors} = require('./components/cors')

try {
    const profiler = logger.startTimer()
    logger.info("Setup Server...")
    app.use(cors())
    // app.use(new DDoS({maxWeight: 5, errorData: {"response": 429, "message": "slow down"}}).express())
    app.use(helmet())
    app.use(bodyParser.json({limit: '512mb'}))
    app.use(bodyParser.urlencoded({limit: '512mb', extended: true}))
    logger.info("Starting Rain...")
    // rain
    // Will contain the event-loop for data collection
    logger.info("Rain Started")
    app.use('/', index)
    app.use('/ec', ec)
    app.set('port', PORT)
    logger.info(`Listening on port ${PORT}`)
    http.listen(PORT)
    logger.info(`Server setup complete`)
    profiler.done({message: `Startup`})
} catch (e) {
    logger.error(e.stack)
}