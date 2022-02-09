"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  var x = 0;
  var y = 0
  var cnt = 0;
  input = input.trim().split('\n');
  var s, t;
  s = input[0];
  t = int(input[1]);
  for (var c of s) {
    if (c === 'U') {
      y++;
    } else if (c === 'D') {
      y--;
    } else if (c === 'R') {
      x++;
    } else if (c === 'L') {
      x--;
    } else {
      cnt++;
    }
  }
  var d = Math.abs(x) + Math.abs(y);
  if (t === 1) {
    d += cnt;
  } else {
    d -= cnt;
  }
  d < 0 ? d &= 1: null;
  console.log(d);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
