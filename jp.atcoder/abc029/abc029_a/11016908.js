"use strict";
const fs = require('fs');

function main(input) {
  var s = input.trim();
  console.log(s + 's');
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
