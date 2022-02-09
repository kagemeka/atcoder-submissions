"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  var a, b, c;
  input = input.trim().split(' ').map(n => int(n));
  a = input[0];
  b = input[1];
  c = input[2];
  var ans = (a*b + b*c + c*a) * 2;
  console.log(ans);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
