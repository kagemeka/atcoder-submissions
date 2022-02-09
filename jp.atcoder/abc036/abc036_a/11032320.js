"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split(' ');
  var a, b;
  a = input[0];
  b = input[1];
  var ans = Math.ceil(b / a);
  console.log(ans);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
