const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split('\n');
  var s, t;
  s = input[0];
  t = input[1];
  var ans;
  (s.length > t.length) ? ans = s : ans = t;
  console.log(ans);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
