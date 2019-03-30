"use strict"

const {logger} = require('./logger')
const axios = require('axios')
const fs = require('fs')
const path = require("path")

class RAIN {
    constructor() {
       
    }
    static getInstance() {
        if (!!!this.instance) {
            this.instance = new RAIN()
        }
        return this.instance
    }
}

module.exports = {
    RAIN
}