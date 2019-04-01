"use strict"
const { 
    api_general,
    api_forecast,
    api_predictions,
    api_giveMeAllYouGot
} = require('../components/api_components')
const express = require('express')
let app = express.Router()

app.get('/', api_general)
app.get('/forecast', api_forecast)
app.post('/predictions', api_predictions)
app.get('/gmayg', api_giveMeAllYouGot)

module.exports = app
