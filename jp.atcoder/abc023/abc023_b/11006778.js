"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  const next = new Map([['b', 'c'], ['c', 'a'], ['a', 'b']]);
  input = input.trim().split('\n');
  var n = int(input[0]);
  var s = input[1];

  if (!(n & 1)) {
    console.log(-1);
    return;
  }
  const first = 'bac';
  var m = (n - 1) / 2
  var nex = first[m % 3];
  for (var c of s) {
    if (c === nex) {
      nex = next.get(c);
    } else {
      console.log(-1);
      return;
    }
  }
  console.log(m);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
