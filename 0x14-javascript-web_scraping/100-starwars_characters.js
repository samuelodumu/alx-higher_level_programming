#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(endpoint, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const characterUrl = body.characters;
  for (const person of characterUrl) {
    request.get(person, { json: true }, (err, res, body1) => {
      if (err) console.log(err);
      console.log(body1.name);
    });
  }
});
