#!/usr/bin/node

let logNo = 0;

function logMe (item) {
  console.log(logNo + ': ' + item);
  logNo++;
}

module.exports = { logMe };
