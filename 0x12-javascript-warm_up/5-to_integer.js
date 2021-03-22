#!/usr/bin/node

const firstArg = process.argv[2];

const isInt = parseInt(firstArg);

if (Number.isNaN(isInt)) console.log('Not a number');
else console.log(`My number: ${isInt}`);
