"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function intArr(arr) {
  return arr.map(n => int(n));
}

function reverseString(s) {
  return s.split('').reverse().join('');
}

function arrMin(arr) {
  return Math.min.apply(Math, arr);
}

function arrMax(arr) {
  return Math.max.apply(Math, arr);
}

function enumerate(arr, start) {
  var res = [];
  (start === undefined) ? start = 0: null;
  for (var i = 0; i < arr.length; i++) {
    res.push([i+start, arr[i]]);
  }
  return res;
}

function counter(arr) {
  var cnt = {}
  arr.forEach(v => {
    cnt[v] = (cnt[v] || 0) + 1;
  });
  return cnt;
}

function main(input) {
  input = input.trim().split('\n');
  var s = input[0];
  var n = int(input[1]);
  var lr = input.slice(2);
  lr.forEach(lr => {
    lr = intArr(lr.split(' '));
    var l, r;
    l = lr[0] - 1;
    r = lr[1] - 1;
    s = s.slice(0, l) + reverseString(s.slice(l, r+1)) + s.slice(r+1);
  });
  console.log(s);

}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
