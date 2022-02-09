"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  var x, n;
  x = int(input.trim());
  n = Math.sqrt(Math.sqrt(x));
  console.log(n);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
