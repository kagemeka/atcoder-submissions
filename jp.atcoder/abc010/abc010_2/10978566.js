const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split('\n');
  var n, a;
  n = int(input[0]);
  a = input[1].split(' ').map(n => int(n));
  var res = 0
  var c;
  for (i in a) {
    c = a[i];
    if (c % 2 === 0) {
      c--;
      res++;
    }
    if (c % 3 === 2) {
      c -= 2;
      res += 2;
    }
  }
  console.log(res)
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
