#!/usr/bin/node
/* using API to print the title film  */
const request = require('request');
const url = process.argv[2];
const FilePath = process.argv[3];
const fs = require('fs');

request.get(url, (error, res, body) => {
  if (error) console.log(error);
  else {
    fs.writeFileSync(FilePath, body);
  }
});
