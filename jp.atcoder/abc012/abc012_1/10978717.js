const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split(' ').map(n => int(n));
  var a, b;
  a = input[0];
  b = input[1];
  console.log(b, a);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
