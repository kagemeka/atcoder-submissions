const fs = require('fs');

function main(input) {
  n = parseInt(input[0]);
  // console.log(n);
  var a = input.split('\n')[1].split(' ');
  a = a.map(n => parseInt(n));

  var res = 100;
  for (var i = 0; i < n; i++) {
    var j = a[i];
    var c = 0;
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
