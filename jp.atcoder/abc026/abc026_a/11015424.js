"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  var a = int(input.trim())
  var x = Math.floor(a / 2);
  var y = a - x;
  console.log(x * y);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
