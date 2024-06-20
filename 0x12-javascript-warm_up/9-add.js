#!/usr/bin/node

const process = require('node:process');

const args = process.argv.slice(2);

function add (a, b) {
  const result = a + b;
  console.log(result);
}

add(parseFloat(args[0]), parseFloat(args[1]));
