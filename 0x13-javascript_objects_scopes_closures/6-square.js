#!/usr/bin/node

const sq = require('./5-square');

module.exports = class Square extends sq {
  constructor (size) {
    super(size, size);
  }

  charPrint (char = 'X') {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += char;
      }
      console.log(row);
    }
  }
};
