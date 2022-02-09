const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.split(' ').map(n => int(n));
  var n = input[0];
  var y = input[1] / 1000;

  var tot;
  var i, j, k;
  for (i = 0; i <= n; i++) {
    tot = i * 10;
    if (tot > y) {
      console.log(-1, -1, -1);
      return;
    }
    for (j = 0; j <= n - i; j++) {
      tot = i * 10 + j * 5;
      if (tot > y) {
        break;
      }
      k = n - i - j;
      tot = i * 10 + j * 5 + k;
      if (tot === y) {
        console.log(i, j, k);
        return;
      }
    }
  }
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
