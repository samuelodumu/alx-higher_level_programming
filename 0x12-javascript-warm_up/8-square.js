#!/usr/bin/node

const process = require('node:process');

const args = process.argv.slice(2);

const argToInt = parseFloat(args[0]);

if (isNaN(argToInt)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argToInt; i++) {
    let output = '';
    for (let j = 0; j < argToInt; j++) {
      output += 'X';
    }
    console.log(output);
  }
}
