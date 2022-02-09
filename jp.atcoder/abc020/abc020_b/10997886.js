"use strict";
const fs = require('fs');

function main(input) {
  input = input.trim().split(' ')
  var n = parseInt(input.join(''), 10);
  console.log(n * 2);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
