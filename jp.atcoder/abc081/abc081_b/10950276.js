const fs = require('fs');

function main(input) {
  n = parseInt(input[0]);
  var a = input.split('\n')[1].split(' ');
  a = a.map(n => parseInt(n));

  let res = 100;
  let j;
  let c;
  for (i = 0; i < n; i++) {
    j = a[i];
    c = 0;
    while (j % 2 === 0) {
      j /= 2;
      c++;
    }
    res = Math.min(res, c);
  }
  console.log(res);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
