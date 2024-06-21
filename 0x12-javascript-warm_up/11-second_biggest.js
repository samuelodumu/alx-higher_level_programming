#!/usr/bin/node

const process = require('node:process');

const args = process.argv.slice(2);

const numbers = [];

if (args.length < 2) {
  console.log(0);
  process.exit();
}

for (const arg of args) {
  numbers.push(arg);
}

let largest = -Infinity;
let secondLargest = -Infinity;

for (const number of numbers) {
  if (parseInt(number) > largest) {
    secondLargest = largest;
    largest = parseInt(number);
  } else if (parseInt(number) < largest && parseInt(number) > secondLargest) {
    secondLargest = parseInt(number);
  }
}

console.log(secondLargest);
