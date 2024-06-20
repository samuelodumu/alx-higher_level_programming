#!/usr/bin/node

const process = require('node:process');

const args = process.argv.slice(2);

const argToInt = parseFloat(args[0]);

if (isNaN(argToInt)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < argToInt; i++) {
    console.log('C is fun');
  }
}
