#!/usr/bin/node

const process = require('node:process');
const args = process.argv.slice(2);
const fs = require('fs');

const filePath = args[0];
const content = args[1];

fs.writeFile(filePath, content, (err) => {
  if (err) {
    console.log(err);
  }
});
