"use strict";
const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  var n = int(input.trim());
  var ans;
  if (n < 60) {
    ans = 'Bad';
  } else if (n < 90) {
    ans = 'Good';
  } else if (n < 100) {
    ans = 'Great';
  } else {
    ans = 'Perfect';
  }
  console.log(ans);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
