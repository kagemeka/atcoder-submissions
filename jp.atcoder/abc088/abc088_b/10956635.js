const fs = require('fs');

function main(input) {
  var arr = input.split('\n')
  var N = parseInt(arr[0], 10);
  var a = arr[1].split(' ')
  a = a.map(n => parseInt(n, 10));
  a.sort().reverse();

  var sa = 0;
  var sb = 0;
  a.forEach((v, i) => {
    (i & 1) ? sb += v : sa += v;
  });
  var ans = sa - sb;
  console.log(ans);
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
