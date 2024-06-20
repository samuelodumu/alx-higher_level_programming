#!/usr/bin/node

const process = require('node:process');

const args = process.argv.slice(2);

function factorial (a) {
  if (isNaN(a) || a === 0) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
}

console.log(factorial(args[0]));
