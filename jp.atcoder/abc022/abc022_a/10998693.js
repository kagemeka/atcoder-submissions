"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split('\n');
  var nst, n, s, t, w, a;
  nst = input[0]; w = input[1]; a = input.slice(2);
  nst = nst.split(' ').map(n => int(n));
  n = nst[0]; s = nst[1]; t = nst[2];
  w = int(w);
  a = a.map(n => int(n));

  var cnt = 0;
  (s <= w && w <= t) ? cnt++: null;
  for (var i of a) {
    w += i;
    (s <= w && w <= t) ? cnt++: null;
  }
  console.log(cnt);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
