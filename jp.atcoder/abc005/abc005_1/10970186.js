const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  var x, y;
  input = input.trim().split(' ').map(n => int(n));
  x = input[0];
  y = input[1];
  console.log(Math.floor(y / x));
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
