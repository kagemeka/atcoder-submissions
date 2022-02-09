"use strict";
const fs = require('fs');

function main(input) {
  input = input.trim().split('\n');
  var n = parseInt(input[0], 10);
  var s = input.slice(1);

  var res = [];
  for (var i = 0; i < n; i++) {
    res[i] = [];
  }

  for (var i = 0; i < n; i++) {
    for (var j = 0; j < n; j++) {
      res[j][n-1-i] = s[i][j];
    }
  }

  for (var i = 0; i < n; i++) {
    console.log(res[i].join(''));
  }
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
