const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  var n = int(input.trim());
  var res = (n + 1) / 2 * 10000;
  console.log(res);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
