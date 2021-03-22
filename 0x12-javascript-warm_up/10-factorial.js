#!/usr/bin/node

const firstArg = process.argv[2];

const isInt = parseInt(firstArg);

function factorial (number) {
  if (number === 0) return 1;
  return number * factorial(number - 1);
}

if (Number.isNaN(isInt)) console.log(1);
else {
  console.log(factorial(isInt));
}
