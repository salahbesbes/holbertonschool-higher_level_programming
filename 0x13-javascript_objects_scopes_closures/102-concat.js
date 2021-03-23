#!/usr/bin/node
'use strict';
const fs = require('fs').promises;

const fileA = process.argv[2];
const fileB = process.argv[3];
const dest = process.argv[4];

async function copyFiles (fileA, fileB, dest) {
  if (!fileA || !fileB || !dest) return;
  try {
    let content = '';
    content += await fs.readFile(fileA);
    content += await fs.readFile(fileB);
    await fs.writeFile(dest, content);
  } catch (error) {
    console.error(`Got an error : ${error.message}`);
    console.log(error);
  }
}

copyFiles(fileA, fileB, dest);
