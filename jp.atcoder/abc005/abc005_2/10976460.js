const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function arrMin(arr) {
  return Math.min.apply(Math, arr);
}

function main(input) {
  var t = input.trim().split('\n').map(n => int(n)).slice(1);
  console.log(arrMin(t));
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
