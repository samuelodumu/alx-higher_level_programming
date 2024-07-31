#!/usr/bin/node

const process = require('node:process');
const args = process.argv.slice(2);
const request = require('request');

const url = args[0];
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  if (response) {
    console.log('code:', response.statusCode);
  }
});
