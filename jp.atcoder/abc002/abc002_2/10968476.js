const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  var w = input.trim().split('');
  var res = '';
  const vowel = new Set('aiueo');

  w.forEach((c) => {
    if (!vowel.has(c)) {
      res += c;
    }
  });
  console.log(res);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
