#!/usr/bin/node
const list = require('./100-data').list;

const newArr = list.map((el, i) => el * i);

console.log(list);
console.log(newArr);
