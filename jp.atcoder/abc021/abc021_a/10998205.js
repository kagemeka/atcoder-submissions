"use strict";
const fs = require('fs');

function main(input) {
  var n = parseInt(input.trim(), 10);
  var res = [];
  var cnt = 0
  while (n !== 0) {
    var r = n % 2;
    n = Math.floor(n / 2);
    res.push(r);
    cnt += r;
  }
  res = res.reverse();
  console.log(cnt);
  for (var i in res) {
    (res[i] === 1) ? console.log(Math.pow(2, i)) : null;
  }
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
