const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function reverseString(s) {
  return s.split('').reverse().join('');
}

function main(input) {
  var grid = input.trim().split('\n');
  grid.reverse();
  grid.forEach(s => {
    console.log(reverseString(s));
  });
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
