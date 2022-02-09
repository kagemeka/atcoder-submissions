"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function enumerate(arr, start) {
  var res = [];
  (start === undefined) ? start = 0: null;
  for (var i = 0; i < arr.length; i++) {
    res.push([i+start, arr[i]]);
  }
  return res;
}

function main(input) {
  var a = input.trim().split('\n').map(n => int(n));
  a = enumerate(a);
  a = a.sort((a, b) => b[1] - a[1]);
  var res = new Array(3).fill(null);
  for (var i = 0; i < 3; i++) {
    res[a[i][0]] = i + 1;
  }
  res.forEach(r => console.log(r));
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
