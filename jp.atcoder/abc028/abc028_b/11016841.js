"use strict";
const fs = require('fs');

function main(input) {
  var s = input.trim()
  var res = new Map();
  for (var c of 'ABCDEF') {
    res[c] = 0;
  }
  for (var c of s) {
    res[c] += 1;
  }

  var ans = [];
  for (var c in res) {
    ans.push(res[c].toString(10));
  }
  console.log(ans.join(' '));
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
