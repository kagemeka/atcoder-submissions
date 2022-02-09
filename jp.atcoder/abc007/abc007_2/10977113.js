const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  var s = input.trim();
  var ans;
  if (s === 'a') {
    ans = -1;
  } else {
    ans = 'a';
  }
  console.log(ans);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
