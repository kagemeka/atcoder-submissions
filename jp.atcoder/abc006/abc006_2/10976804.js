const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

const mod = 10007;
var n = 10 ** 6;
var tribonacci = new Array(n+1).fill(null);
tribonacci[0] = 0;
tribonacci[1] = 0;
tribonacci[2] = 1;
for (var i = 3; i <= n; i++) {
  tribonacci[i] = tribonacci[i-3] + tribonacci[i-2] + tribonacci[i-1]
  tribonacci[i] %= mod;
}

function main(input) {
  n = int(input.trim());
  console.log(tribonacci[n-1])
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
