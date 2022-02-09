const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split('\n');
  var n, a;
  n = int(input[0]);
  a = input[1].split(' ').map(n => int(n));
  var cnt = 0;
  var tot = 0;
  for (i in a) {
    if (a[i]) {
      tot += a[i];
      cnt++;
    }
  }
  console.log(Math.ceil(tot / cnt));
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
