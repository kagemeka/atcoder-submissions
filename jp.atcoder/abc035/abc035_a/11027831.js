"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split(' ').map(n => int(n));
  var w, h;
  w = input[0]; h = input[1];
  var ans = w/h === 4/3? '4:3': '16:9';
  console.log(ans);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
