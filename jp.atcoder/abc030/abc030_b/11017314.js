"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  var n, m;
  input = input.trim().split(' ').map(n => int(n)) ;
  n = input[0];
  m = input[1];
  var a, b;
  b = m * 6;
  n = n % 12;
  a = 30 * (n + m / 60);
  var d = Math.abs(b - a);
  var ans = Math.min(360 - d, d);
  console.log(ans);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
