#!/usr/bin/node

const Rectangle = require('./demo');

class Square extends Rectangle {
  constuctor (size) {
    super(size, size);
  }
}

module.exports = Square
