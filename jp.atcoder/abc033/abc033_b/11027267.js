"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split('\n');
  var n, sp;
  n = int(input[0]);
  sp = input.slice(1);

  var tot = 0;
  sp.forEach(sp => {
    var sp = sp.split(' ');
    var p;
    p = int(sp[1]);
    tot += p;
  });

  var half = tot / 2;

  for (var x of sp) {
    x = x.split(' ');
    var s, p;
    s = x[0];
    p = int(x[1]);
    if (p >= half) {
      console.log(s);
      return;
    }
  }
  console.log('atcoder');
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
