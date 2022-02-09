const fs = require('fs');

function main(input) {
  var [n, a, b] = input.trim().split(' ');
  [n, a, b] = [Number(n), Number(a), Number(b)];
  var c = a + b;
  console.log(c);
  var [q, r] = [Math.floor(n / c), n % c];
  var res = a * q + Math.min(r, a);
  console.log(res);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);