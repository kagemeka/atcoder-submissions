"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split(' ').map(n => int(n));
  var a, b, c;
  a = input[0];
  b = input[1];
  c = input[2];
  var ans;
  if (a === b) {
    ans = c;
  } else {
    if (a === c) {
      ans = b;
    } else {
      ans = a;
    }
  }
  console.log(ans);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
