#!/usr/bin/node

exports.addMeMaybe = function (n, func) {
  func(++n);
};
