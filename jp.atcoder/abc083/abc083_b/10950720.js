const fs = require('fs');

function divmod(a, b) {
  var q = Math.floor(a / b);
  var r = a % b;
  return [q, r]
}

function main(input) {
  var arr = input.split(' ');
  var [n, a, b] = arr.map((n) => parseInt(n, 10));

  var res = 0;
  var tot;
  var q, r;
  for (var i = 0; i <= n; i++) {
    q = i;
    tot = 0;
    while (q !== 0) {
      [q, r] = divmod(q, 10);
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
