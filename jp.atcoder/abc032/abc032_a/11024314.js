"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function gcd(a, b) {
  var c;
  while (b) {
    c = b;
    b = a % b;
    a = c;
  }
  return a;
}

function lcm(a, b) {
  return a / gcd(a, b) * b;
}

function main(input) {
  input = input.trim().split('\n').map(n => int(n));
  var a, b, n;
  a = input[0];
  b = input[1];
  n = input[2];
  var l = lcm(a, b);
  function binary_search(b) {
    return l * b >= n;
  }
  var lo = 0; var hi = n;
  while (lo + 1 < hi) {
    var m = Math.floor((lo + hi) / 2);
    binary_search(m) ? hi = m: lo = m;
  }
  var ans = l * hi;
  console.log(ans);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
