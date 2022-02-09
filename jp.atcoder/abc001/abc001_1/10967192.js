const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  var h1, h2;
  input = input.split('\n').map(n => int(n));
  h1 = input[0];
  h2 = input[1];
  console.log(h1 - h2);

}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
