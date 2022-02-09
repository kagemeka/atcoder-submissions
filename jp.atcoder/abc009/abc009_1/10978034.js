const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  var n = int(input.trim());
  var res = Math.ceil(n / 2);
  console.log(res);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
