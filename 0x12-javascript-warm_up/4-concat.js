#!/usr/bin/node

const firstArg = process.argv[2] || 'undefined';
const secondArg = process.argv[3] || 'undefined';

console.log(`${firstArg} is ${secondArg}`);
