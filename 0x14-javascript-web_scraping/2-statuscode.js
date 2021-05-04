#!/usr/bin/node
/* display the status code of a request  */
const request = require('request');
const url = process.argv[2];

request.get(url, (error, res, body) => {
  if (error) console.log(error);
  else console.log(`code: ${res.statusCode}`);
});
