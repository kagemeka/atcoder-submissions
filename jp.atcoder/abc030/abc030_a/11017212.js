"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split(' ').map(n => int(n));
  var a, b, c, d, p1, p2;
  a = input[0]; b = input[1]; p1 = b / a;
  c = input[2]; d = input[3]; p2 = d / c;
  var ans;
  if (p1 > p2) {
    ans = 'TAKAHASHI';
  } else if (p1 === p2) {
    ans = 'DRAW';
  } else {
    ans = 'AOKI';
  }
  console.log(ans);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
