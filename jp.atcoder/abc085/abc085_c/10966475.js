const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.split(' ').map(n => int(n));
  var n = input[0];
  var y = input[1] / 1000;

  var tot;
  for (var i = 0; i <= n; i++) {
    tot = i * 10;
    if (tot > y) {
      console.log(-1, -1, -1);
      return;
    }
    for (var j = 0; j <= n - i; j++) {
      tot = i * 10 + j * 5;
      if (tot > y) {
        break;
      }
      for (var k = 0; k <= n - i - j; k++) {
        tot = i * 10 + j * 5 + k;
        if (tot > y) {
          break;
        }
        if (tot === y) {
          console.log(i, j, k);
          return
        }
      }
    }
  }
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
