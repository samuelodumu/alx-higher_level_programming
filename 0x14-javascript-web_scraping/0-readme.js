#!/usr/bin/node

const process = require('node:process');
const args = process.argv.slice(2);
const fs = require('fs');

const filePath = args[0];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
