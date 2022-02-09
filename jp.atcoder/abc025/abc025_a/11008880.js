"use strict";
const fs = require('fs');

var res = [];
function product(s, cand, repeat) {
  if (s.length === repeat) {
    res.push(s);
  } else {
    var t;
    for (var c of cand) {
      t = s + c;
      product(t, cand, repeat);
    }
  }
}

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split('\n');
  var s = input[0];
  var n = int(input[1]);
  product('', s, 2);
  console.log(res[n-1]);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
