#!/usr/bin/node
/* using API to print the title film  */
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;
/* create a mapped dict for completed tasks */
request.get(url, (error, res) => {
  if (error) console.log(error);
  else {
    const result = JSON.parse(res.body);

    result.characters.forEach((apiChar) => {
      request.get(apiChar, (error, res) => {
        if (error) throw error;
        else {
          const result2 = JSON.parse(res.body);
          console.log(result2.name);
        }
      });
    });
  }
});
