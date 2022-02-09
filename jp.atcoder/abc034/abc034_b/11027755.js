"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  var n = int(input.trim());
  var m = n & 1? n + 1: n - 1;
  console.log(m);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
