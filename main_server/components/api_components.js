"use strict"

const axios = require('axios')
const {logger} = require('./logger')
const rain = require('./rain').RAIN.getInstance()

const api_general = (req, res, next) => {
    return res.json({response: 200})
}

const api_predictions = (req, res, next) => {
    var predicted_data = req.body.data
    console.log({"body": req.body})
    rain.hasPredictedData(predicted_data)
    return res.json({response: 200, message: "Data received!", len: predicted_data.length})
}

const api_giveMeAllYouGot = (req, res, next) => {
    let now = new Date()
    return res.json({now})
}

module.exports = {
    api_general,
    api_predictions,
    api_giveMeAllYouGot
}