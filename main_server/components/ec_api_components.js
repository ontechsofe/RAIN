"use strict"

const axios = require('axios')
const {logger} = require('./logger')

const api_general = (req, res, next) => {
    return res.json({response: 200, message: "Welcome to the root of the EC route"})
}

const api_getWeather = (req, res, next) => {
    axios.get(`http://localhost:6969/get`).then(response => {
        return res.json({response: 200, message: response.data})
    }).catch(error => {
        logger.error(error.stack)
    })
}

const api_getPastWeather = (req, res, next) => {
    let epoch = req.params.epoch, off = req.params.offset
    axios.get(`http://localhost:6969/past/${epoch}/${off}`).then(response => {
        return res.json({response: 200, message: response.data})
    }).catch(error => {
        logger.error(error.stack)
    })
}

module.exports = {
    api_general,
    api_getWeather,
    api_getPastWeather
}