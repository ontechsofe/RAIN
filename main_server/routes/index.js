"use strict"
const { 
    api_general,
    api_giveMeAllYouGot
} = require('../components/api_components')
const express = require('express')
let app = express.Router()

app.get('/', api_general)
app.get('/gmayg', api_giveMeAllYouGot)

module.exports = app