#!/usr/bin/node
/* using API to print the title film  */
const request = require('request');
const url = process.argv[2];
/* create a mapped dict for completed tasks */
request.get(url, (error, res, body) => {
  if (error) console.log(error);
  else {
    const result = JSON.parse(res.body);
    const dict = {};

    result.forEach((element) => {
      if (!dict[element.userId]) dict[element.userId] = 0;
      if (element.completed === true) dict[element.userId]++;
    });
    console.log(dict);
  }
});
