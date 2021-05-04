#!/usr/bin/node
/* using API to print the title film  */
const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request.get(url, (error, res, body) => {
  if (error) console.log(error);
  else console.log(`${JSON.parse(res.body).title}`);
});
