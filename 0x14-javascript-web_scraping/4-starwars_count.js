#!/usr/bin/node
/* using API to print the title film  */
const request = require('request');
const url = process.argv[2];
/*
request.get(url, (error, res) => {
  if (error) console.log(error);
  else {
    const result = JSON.parse(res.body);

    const nbFound = result.results.reduce(
      // sum of results array
      (total, element) =>
        total +
        // sum of characters array
        element.characters.reduce(
          (total, endPoint) =>
            endPoint === 'https://swapi-api.hbtn.io/api/people/18/'
              ? total + 1
              : total,
          0
        ),
      0
    );
    */
request.get(url, (error, res) => {
  let nbFound = 0;
  if (error) console.log(error);
  else {
    const result = JSON.parse(res.body);
    result.results.forEach((film) => {
      film.characters.forEach((endPoint) => {
        if (endPoint === 'https://swapi-api.hbtn.io/api/people/18/') nbFound++;
      });
    });
    console.log(nbFound);
  }
});
