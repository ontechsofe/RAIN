"use strict"

const {logger} = require('./logger')
const axios = require('axios')
const fs = require('fs')
const path = require("path")

const db = require('./database').Database.getInstance()

class RAIN {
    constructor() {
        this.database = db
    }
    static getInstance() {
        if (!!!this.instance) {
            this.instance = new RAIN()
        }
        return this.instance
    }
    hasPredictedData(data) {
        logger.info("Predicted Data Received")
        console.log(data)
        this.database.insertPredictedData(data)
        logger.info("Predicted Data Complete")
    }
}

module.exports = {
    RAIN
}