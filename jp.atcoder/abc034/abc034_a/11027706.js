"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split(' ').map(n => int(n));
  var x, y;
  x = input[0];
  y = input[1];
  var ans = y > x? 'Better': 'Worse';
  console.log(ans);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
