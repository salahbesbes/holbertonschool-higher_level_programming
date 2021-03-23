#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const newlist = list.filter((el) => searchElement === el);
  return newlist.length;
};
