"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  var a = int(input.trim())
  var ans = Math.floor(a*a/4);
  console.log(ans);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
