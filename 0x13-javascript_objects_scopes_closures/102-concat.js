#!/usr/bin/node

/*
const fs = require('fs').promises;

const fileA = process.argv[2];
const fileB = process.argv[3];
const dest = process.argv[4];

async function copyFiles(fileA, fileB, dest) {
  if (!fileA || !fileB || !dest) return;
  try {
    let content = '';
    content += await fs.readFile(fileA);
    content += await fs.readFile(fileB);
    await fs.writeFile(dest, content);
  } catch (error) {}
}

copyFiles(fileA, fileB, dest);

*/

const fs = require('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];
const dest = process.argv[4];
let content = fs.readFileSync(fileA, 'utf8');
content += fs.readFileSync(fileB, 'utf-8');
fs.writeFileSync(dest, content);
