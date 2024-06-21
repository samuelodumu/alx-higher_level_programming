#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((!w || !h) || (w <= 0 || h <= 0)) {
      return Object.assign(this, {});
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      let row = '';
      for (let y = 0; y < this.width; y++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  double () {
    this.height *= 2; // this.height = this.height * 2
    this.width *= 2;
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
}

module.exports = Rectangle;

// double()
// rotate()
