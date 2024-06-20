#!/usr/bin/node

const process = require('node:process');

const args = process.argv.slice(2);

if (args[0] == null) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
