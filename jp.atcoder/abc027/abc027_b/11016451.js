"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function arrSum(arr) {
  return arr.reduce((a, b) => a + b);
}

function main(input) {
  input = input.trim().split('\n');
  var n, a;
  n = int(input[0]);
  a = input[1].split(' ').map(n => int(n));
  var s = arrSum(a);
  if (s % n) {
    console.log(-1);
    return;
  }

  var cap = s / n;
  a = [0].concat(a);
  for (var i = 1; i <=n; i++) {
    a[i] += a[i-1];
  }
  var last = 0;
  var res = 0;
  while (last < n) {
    for (var i = last + 1; i <= n; i++) {
      if ((a[i] - a[last]) / (i - last) === cap) {
        res += i - last - 1;
        last = i;
        break;
      }
    }
  }
  console.log(res);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
