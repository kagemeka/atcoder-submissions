const fs = require('fs');

function main(input) {
  var a = input.split('\n')[1].split(' ');
  a = a.map((n) => parseInt(n, 10));

  var cnt = 0;
  while (a.every((n) => (n % 2) === 0)) {
    cnt++;
    a = a.map((n) => n / 2);
  }
  console.log(cnt);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
