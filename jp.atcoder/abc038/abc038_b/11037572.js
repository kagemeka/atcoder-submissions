"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split('\n');
  var a, b;
  a = input[0].split(' ').map(n => int(n));
  b = input[1].split(' ').map(n => int(n));

  for (var x of a) {
    for (var y of b) {
      if (x === y) {
        console.log('YES');
        return;
      }
    }
  }
  console.log('NO');
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
