const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split('\n');
  var s, t;
  s = input[0];
  t = input[1];
  n = s.length;

  var joker = new Set('atcoder@');
  for (var i = 0; i < n; i++) {
    if (s[i] !== t[i]) {
      if (s[i] === '@' && joker.has(t[i])) {
        continue;
      } else if (t[i] === '@' && joker.has(s[i])) {
        continue;
      } else {
        console.log('You will lose');
        return;
      }
    }
  }
  console.log('You can win');
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
