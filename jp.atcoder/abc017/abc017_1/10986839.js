const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split('\n');
  var res = 0;
  for (i in input) {
    var se = input[i];
    se = se.split(' ').map(n => int(n));
    s = se[0];
    e = se[1];
    res += s * e / 10;
  }
  console.log(res);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
