#!/usr/bin/node

const length = process.argv.length;
if (length === 3) console.log('Argument found');
else if (length > 3) console.log('Arguments found');
else console.log('No argument');
