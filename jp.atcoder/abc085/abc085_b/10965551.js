const fs = require('fs');

function main(input) {
  var arr = input.split('\n');
  var n = parseInt(arr[0], 10);
  var d = arr.slice(1, -1).map(n => parseInt(n, 10));
  d.sort((a, b) => b - a);

  var cur = Infinity;
  var cnt = 0;
  for (var i = 0; i < n; i++) {
    (d[i] < cur) ? cnt++ : NaN;
    cur = d[i];
  }
  console.log(cnt);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
