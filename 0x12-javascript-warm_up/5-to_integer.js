#!/usr/bin/node

const process = require('node:process');

const args = process.argv.slice(2);

const argToInt = parseFloat(args[0]);

if (isNaN(argToInt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argToInt);
}
