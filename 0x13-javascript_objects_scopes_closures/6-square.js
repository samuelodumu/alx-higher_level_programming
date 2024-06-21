#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let output = '';
      for (let j = 0; j < this.width; j++) {
        if (c === undefined) {
          output += 'X';
        } else {
          output += c;
        }
      }
      console.log(output);
    }
  }
}

module.exports = Square;
