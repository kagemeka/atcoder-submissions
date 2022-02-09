const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  n = int(input.trim());
  console.log((n + 1) % 13);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
