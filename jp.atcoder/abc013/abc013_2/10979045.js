const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split('\n').map(n => int(n));
  var a, b;
  a = input[0];
  b = input[1];
  var ans;
  if (b >= a) {
    ans = Math.min(b - a, a - (b - 10));
  } else {
    ans = Math.min(a - b, b + 10 - a);
  }
  console.log(ans);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
