"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split('\n');
  var nab, n, a, b, sd;
  nab = input[0].split(' ').map(n => int(n));
  n = nab[0]; a = nab[1]; b = nab[2];
  sd = input.slice(1);
  var res = 0;
  sd.forEach(sd => {
    var s, d;
    sd = sd.split(' ');
    s = sd[0]; d = int(sd[1]);
    d = Math.min(b, Math.max(a, d));
    res += s === 'East' ? d: -d;
  });
  if (res === 0) {
    console.log(0);
  } else {
    var direction;
    if (res > 0) {
      direction = 'East';
    } else {
      direction = 'West';
      res *= -1;
    }
    console.log(`${direction} ${res}`);
  }
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
