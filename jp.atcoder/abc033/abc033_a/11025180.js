"use strict";
const fs = require('fs');

function main(input) {
  var s = input.trim();
  var res = new Set(s);
  var ans = res.size === 1 ? 'SAME': 'DIFFERENT';
  console.log(ans);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
