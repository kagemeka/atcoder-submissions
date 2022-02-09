"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split('\n');
  var n, ab, a, b, k, p;
  n = int(input[0]);
  ab = input[1].split(' ').map(n => int(n));
  a = ab[0];
  b = ab[1];
  k = int(input[2]);
  p = input[3].split(' ').map(n => int(n));
  var cities = new Set(p);
  cities.add(a); cities.add(b);
  var ans = (cities.size === k + 2) ? 'YES' : 'NO';
  console.log(ans);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
