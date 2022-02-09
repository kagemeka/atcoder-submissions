"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split(' ').map(n => int(n));
  var a, b, c;
  a = input[0];
  b = input[1];
  c = input[2];
  var ans = Math.floor(c / Math.min(a, b));
  console.log(ans);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
