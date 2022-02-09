const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  var s, t;
  input = input.trim().split(' ').map(n => int(n));
  s = input[0];
  t = input[1];
  console.log(t - s + 1);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
