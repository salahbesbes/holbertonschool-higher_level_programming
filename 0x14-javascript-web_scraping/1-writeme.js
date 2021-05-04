#!/usr/bin/node
/* write the content of a file  */
const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];
/* write into file syncro way */
fs.writeFileSync(filePath, content);
