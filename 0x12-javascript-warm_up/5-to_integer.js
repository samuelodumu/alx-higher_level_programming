#!/usr/bin/node

const process = require('node:process');

const args = process.argv.slice(2);

let argToInt = parseFloat(args[0]);

if (typeof (argToInt !== 'number')) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argToInt);
}
