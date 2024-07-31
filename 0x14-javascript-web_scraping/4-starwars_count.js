#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');

const endpoint = args[0];
request.get(endpoint, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  console.log(body)
  const count = body.split('people/18').length - 1
  console.log(count);
});
