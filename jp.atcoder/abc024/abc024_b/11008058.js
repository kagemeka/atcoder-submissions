"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}
function main(input) {
  input = input.trim().split('\n');
  var nt, n, t, a;
  nt = input[0].split(' ').map(n => int(n));
  n = nt[0];
  t = nt[1];
  a = input.slice(1).map(n => int(n));
  var tot = 0;
  var start = a[0];
  a.slice(1).forEach(a => {
    tot += Math.min(t, a - start);
    start = a;
  });
  tot += t;
  console.log(tot);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
