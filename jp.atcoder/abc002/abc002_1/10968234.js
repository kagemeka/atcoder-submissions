const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.split(' ').map(n => int(n));
  var x, y;
  x = input[0];
  y = input[1];
  var res;
  (x >= y) ? res = x : res = y;
  console.log(res);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
