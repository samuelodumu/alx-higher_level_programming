#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');

const id = args[0];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${id}`;
request.get(endpoint, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  console.log(body.title);
});
