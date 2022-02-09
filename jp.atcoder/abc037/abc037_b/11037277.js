"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split('\n');
  var nq, n, q, lrt;
  nq = input[0].split(' ').map(n => int(n));
  n = nq[0];
  q = nq[1];
  lrt = input.slice(1);
  var a = new Array(n).fill(0);

  for (var x of lrt) {
    var l, r, t;
    x = x.split(' ').map(n => int(n));
    l = x[0];
    r = x[1];
    t = x[2];
    for (var i = l-1; i < r; i++) {
      a[i] = t;
    }
  }
  for (var x of a) {
    console.log(x);
  }
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
