const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  var x = input.trim();
  var res = x.charCodeAt(0) - 64;
  console.log(res);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
