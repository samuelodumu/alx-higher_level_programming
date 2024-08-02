#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(endpoint, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  console.log(body.title);
});
