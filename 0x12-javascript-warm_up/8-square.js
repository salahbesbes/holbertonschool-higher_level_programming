#!/usr/bin/node

const firstArg = process.argv[2];

const size = parseInt(firstArg);

if (Number.isNaN(size)) console.log('Missing size');
else {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let i = 0; i < size; i++) {
      row += 'X';
    }
    console.log(row);
  }
}
