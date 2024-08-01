#!/usr/bin/node

// start
// import fs module
// read the file
// display errors (if any)
// print file contents to stdout

const fs = require('fs');
filePath = process.argv[2];

fs.readFile(filePath, 'utf8', function (error, content) {
  if (error) {
    console.log(error);
  }
  console.log(content);
});
