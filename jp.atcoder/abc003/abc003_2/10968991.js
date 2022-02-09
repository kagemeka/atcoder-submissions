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
      if (!(joker.has(s[i]) && joker.has(t[i]))) {
        console.log('You will lose');
        return;
      }
    }
  }
  console.log('Your can win')
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
