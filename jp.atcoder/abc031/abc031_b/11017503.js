"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split('\n');
  var lh, l, h, n, a;
  lh = input[0].split(' ').map(n => int(n));
  l = lh[0];
  h = lh[1];
  n = int(input[1]);
  a = input.slice(2).map(n => int(n));
  a.forEach(t => {
    if (t > h) {
      console.log(-1);
    } else {
      console.log(Math.max(0, l - t));
    }
  });
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
