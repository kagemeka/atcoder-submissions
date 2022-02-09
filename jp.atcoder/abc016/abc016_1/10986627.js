const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split(' ').map(n => int(n));
  var ans;
  (m % d === 0) ? ans = 'YES': ans = 'NO';
  console.log(ans);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
