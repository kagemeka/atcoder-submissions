const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split('\n').map(n => int(n));
  var a, n;
  n = input[0];
  a = input.slice(1);
  a.sort((a, b) => b - a);
  const max = a[0];

  for (var i = 1; i < n; i++) {
    if (a[i] !== max) {
      console.log(a[i]);
      return;
    }
  }
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
