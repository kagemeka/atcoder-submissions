"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  var n = int(input.trim());
  var res = n;

  for (var i = 1; i <= Math.floor(Math.sqrt(n)); i++) {
    var j = Math.floor(n / i);
    var r = n - i * j;
    res = Math.min(res, Math.abs(i - j) + r);
  }
  console.log(res);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
