#!/usr/bin/node
/* read the content of a file  */
const fs = require("fs");

let file_path = process.argv[2];

/* this is asyncrone => code below this function get executed before the data is printed */
fs.readFile(file_path, (encodeURI = "utf-8"), (err, data) => {
  if (err) console.log(err);
  else console.log(data);
});
