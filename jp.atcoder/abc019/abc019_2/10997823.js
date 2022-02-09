"use strict";
const fs = require('fs');

function main(input) {
  var s = input.trim() + '$';
  var prev = s[0];
  var cnt = 1;
  var res = '';
  s.slice(1).split('').forEach(char => {
    if (char === prev) {
      cnt++;
    } else {
      res += prev + cnt.toString(10);
      prev = char;
      cnt = 1;
    }
  });
  console.log(res);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
