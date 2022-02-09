const fs = require('fs');

function main(input) {
  var arr = input.trim().split(' ');
  arr = arr.map(Number);
  var n = arr[0];
  var a = arr[1];
  var b = arr[2];
  var c = a + b;
  var q = Math.floor(n / c);
  var r = n % c;
  res = a * q + Math.min(a, r);
  console.log(res);

}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
