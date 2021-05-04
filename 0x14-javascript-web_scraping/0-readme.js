#!/usr/bin/node
/* read the content of a file  */
const fs = require('fs');
const filePath = process.argv[2];

/* this is asyncrone => code below this function get executed before the data is printed */
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) console.log(err);
  else console.log(data);
});
