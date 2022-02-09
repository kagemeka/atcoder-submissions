"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function sumArr(arr) {
  return arr.reduce((a, b) => a + b);
}

function main(input) {
  var x = input.trim().split('').map(n => int(n));
  var res = sumArr(x);
  console.log(res);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
