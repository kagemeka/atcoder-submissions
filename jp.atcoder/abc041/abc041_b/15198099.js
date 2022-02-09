"use strict";
const fs = require('fs');

const mod = BigInt(1e9+7);
function B(input) {
  var a, b, c;
  input = input.trim().split(' ').map(BigInt);
  [a, b, c] = input;
  var ans = a * b % mod * c % mod;
  ans = Number(ans)
  console.log(ans);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
B(input);
