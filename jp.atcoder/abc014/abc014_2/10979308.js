const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function intArr(arr) {
  return arr.map(n => int(n));
}

function main(input) {
  input = input.trim().split('\n');
  var nx, n, x, a;
  nx = intArr(input[0].split(' '));
  a = intArr(input[1].split(' '));
  n = nx[0];
  x = nx[1];
  var tot = 0;
  for (i in [...Array(n)]) {
    (x >> i & 1) ? tot += a[i] : null;
  }
  console.log(tot);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
