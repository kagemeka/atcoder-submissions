const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  var a, b;
  input = input.trim().split('\n').map(n => int(n));
  a = input[0];
  b = input[1];
  var needed = b * Math.ceil(a / b);
  var res = needed - a;
  console.log(res);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
