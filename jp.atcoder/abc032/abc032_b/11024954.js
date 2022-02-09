"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split('\n');
  var s = input[0];
  var k = int(input[1]);
  var res = new Set();
  var n = s.length;
  if (k > n) {
    console.log(0);
    return;
  }

  for (var i = 0; i < n - k + 1; i++) {
    res.add(s.slice(i, i+k));
  }
  console.log(res.size);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
