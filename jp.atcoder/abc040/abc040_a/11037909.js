"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  var n, x;
  input = input.trim().split(' ').map(n => int(n));
  n = input[0];
  x = input[1];
  console.log(Math.min(n - x, x - 1));
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
