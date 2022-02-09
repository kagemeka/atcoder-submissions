"use strict";
const fs = require('fs');

const mod = 1e9 + 7;
function B(input) {
  var a, b, c;
  input = input.trim().split(' ').map(BigInt);
  [a, b, c] = input;
  console.log(a, b, c)
  var ans = a * b % 100000007n * c % 100000007n;
  console.log(ans);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
B(input);
