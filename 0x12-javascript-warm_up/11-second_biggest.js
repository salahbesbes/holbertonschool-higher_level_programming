#!/usr/bin/node

let args = process.argv;

if (args.length > 3) {
  args = args.sort((a, b) => a - b);
  console.log(args[args.length - 2]);
} else console.log(0);
