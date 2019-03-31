"use strict"
const { 
    api_general,
    api_getWeather,
    api_getPastWeather
} = require('../components/ec_api_components')
const express = require('express')
let app = express.Router()

app.get('/', api_general)
app.get('/get', api_getWeather)
app.get('/past/:epoch/:offset', api_getPastWeather)

module.exports = app