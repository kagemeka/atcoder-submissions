const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  s = input.trim().toLowerCase();
  s = s[0].toUpperCase() + s.slice(1);
  console.log(s);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
