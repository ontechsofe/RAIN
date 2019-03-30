"use strict"

const api_general = (req, res, next) => {
    return res.json({response: 200})
}

const api_giveMeAllYouGot = (req, res, next) => {
    let now = new Date()
    return res.json({now})
}

module.exports = {
    api_general,
    api_giveMeAllYouGot
}