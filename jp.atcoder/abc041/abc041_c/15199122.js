"use strict";
const fs = require('fs');

const mod = BigInt(1e9+7);


function A(input) {
  var s, i
  input = input.trim().split('\n');
  [s, i] = input;
  i = parseInt(i, 10);
  console.log(s[i-1]);
}

function B(input) {
  var a, b, c;
  input = input.trim().split(' ').map(BigInt);
  [a, b, c] = input;
  var ans = a * b % mod * c % mod;
  ans = Number(ans);
  console.log(ans);
}

function C(input) {
  var [n, height] = input.trim().split('\n');
  height = height.split(' ').map(n => parseInt(n, 10));
  n = parseInt(n, 10);
  var height = Object.keys(height).map(key => [parseInt(key, 10)+1, height[key]]);
  height.sort(function(first, second) {
    return (second[1] - first[1]);
  });
  for (var [i, h] of height) {
    console.log(i);
  }
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
// A(input);
// B(input);
C(input);
