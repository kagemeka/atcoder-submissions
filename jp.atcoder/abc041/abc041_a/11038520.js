"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split('\n');
  var s, i;
  s = input[0];
  i = int(input[1]);
  console.log(s[i-1]);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
