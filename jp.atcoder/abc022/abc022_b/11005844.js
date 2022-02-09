"use strict";
const fs = require('fs');

function counter(arr) {
  var cnt = new Map();
  for (var i of arr) {
    cnt[i] = (cnt[i] || 0) + 1;
  }
  return cnt;
}

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split('\n').map(n => int(n));
  var n = input[0];
  var a = input.slice(1);
  var cnt = counter(a);
  var res = 0;
  for (const [k, v] of Object.entries(cnt)) {
    res += v - 1;
  }
  console.log(res);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
