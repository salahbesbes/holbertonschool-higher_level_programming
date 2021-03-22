#!/usr/bin/node

const firstArg = process.argv[2];
const secondArg = process.argv[3];

function add(firstArg, secondArg) {
  const first = parseInt(firstArg);
  const second = parseInt(secondArg);

  if (Number.isNaN(first) || Number.isNaN(second)) console.log(NaN);
  else {
    console.log(`${first + second}`);
  }
}

add(firstArg, secondArg);
