"use strict";
const fs = require('fs');

function main(input) {
  var s = input.trim().split('\n');
  var cnt = 0;
  s.forEach(s => cnt += s.includes('r')? 1: 0);
  console.log(cnt);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
