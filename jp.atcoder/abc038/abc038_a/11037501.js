"use strict";
const fs = require('fs');

function main(input) {
  var s = input.trim()
  var ans = s.slice(-1) === 'T' ? 'YES': 'NO';
  console.log(ans);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
