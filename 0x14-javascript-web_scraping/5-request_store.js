#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const endpoint = process.argv[2];
const filePath = process.argv[3];

request(endpoint).pipe(fs.createWriteStream(filePath));
