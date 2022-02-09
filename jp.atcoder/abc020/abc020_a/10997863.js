"use strict";
const fs = require('fs');

function main(input) {
  var q = parseInt(input.trim());
  var ans;
  (q === 1) ? ans = 'ABC': ans = 'chokudai';
  console.log(ans);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
