const fs = require('fs');

function main(input) {
  var [n, a, b] = input.trim().split(' ');
  console.log(n)
  // [n, a, b] = [Number(n), Number(a), Number(b)];
  // var c = a + b;
  // var [q, r] = [Math.floor(n / c), n % c];
  // var res = a * q + Math.min(r, a);
  // console.log(res);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
