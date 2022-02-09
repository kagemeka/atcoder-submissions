const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split(' ').map(n => int(n));
  var a, b, c;
  a = input[0];
  b = input[1];
  c = input[2];
  var bl1, bl2;
  bl1 = a + b === c;
  bl2 = a - b === c;
  var ans;
  if (bl1) {
    if (bl2) {
      ans = '?';
    } else {
      ans = '+';
    }
  } else {
    if (bl2) {
      ans = '-';
    } else {
      ans = '!'
    }
  }
  console.log(ans)
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
