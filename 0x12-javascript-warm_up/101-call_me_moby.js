#!/usr/bin/node

exports.callMeMoby = function (nb, func) {
  for (let i = 0; i < nb; i++) {
    func();
  }
};
