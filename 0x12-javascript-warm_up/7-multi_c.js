#!/usr/bin/node

const length = process.argv[2];

const isInt = parseInt(length);

if (Number.isNaN(isInt)) console.log('Missing number of occurrences');
else {
  for (let i = 0; i < length; i++) {
    console.log('C is fun');
  }
}
