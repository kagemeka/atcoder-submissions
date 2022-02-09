"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split(' ').map(n => int(n));
  var a, d;
  a = input[0]; d = input[1];
  (a <= d)? a++ : d++;
  console.log(a * d);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
