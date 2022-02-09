"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function circleArea(r) {
  return r * r * Math.PI;
}

function main(input) {
  input = input.trim().split('\n');
  var n, r;
  n = int(input[0]);
  r = input.slice(1).sort((a, b) => a - b);
  var s = r.map(r => circleArea(int(r)));
  s = [0].concat(s);

  var res = 0;
  for (var i = n; i >= 1; i -= 2) {
    res += s[i] - s[i-1];
  }
  console.log(res);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
