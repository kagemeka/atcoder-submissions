"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split('\n');
  var abck, a, b, c, k, st, s, t;
  abck = input[0].split(' ').map(n => int(n));
  st = input[1].split(' ').map(n => int(n));
  a = abck[0];
  b = abck[1];
  c = abck[2];
  k = abck[3];
  s = st[0];
  t = st[1];
  var ans = a*s + b*t
  ans -= (s + t >= k) ? c*(s+t): 0;
  console.log(ans);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
