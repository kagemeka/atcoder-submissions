const fs = require('fs');

function divmod(a, b) {
  var q = Math.floor(a / b);
  var r = a % b;
  return [q, r]
}

function main(input) {
  var arr = input.split(' ');
  arr = arr.map((n) => parseInt(n, 10));
  n = arr[0]; a = arr[1]; b = arr[2];

  var res = 0;
  var tot;
  var q;
  var r;
  var d;
  for (var i = 0; i <= n; i++) {
    q = i;
    tot = 0;
    while (q) {
      d = divmod(q, 10);
      q = d[0]; r = d[1];
      tot += r;
    }
    if (a <= tot && tot <= b) {
      res += i;
    }
  }
  console.log(res);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
