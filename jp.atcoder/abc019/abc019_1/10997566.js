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
  var a = input.trim().split(' ').map(n => parseInt(n, 10));
  a.sort((a, b) => b - a);
  console.log(a[1]);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
