#!/usr/bin/node

const process = require('node:process');

const args = process.argv.slice(2);

const numbers = [];

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  for (const arg of args) {
    numbers.push(arg);
  }
  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (const number of numbers) {
    if (number > largest) {
      secondLargest = largest;
      largest = number;
    } else if (number > secondLargest && number !== largest) {
      secondLargest = number;
    }
  }

  console.log('Second largest number:', secondLargest);
}
