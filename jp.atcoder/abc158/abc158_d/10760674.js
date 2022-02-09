function main(input) {
  data = input.split('\n');
  var res = data[0];
  var n = data[1];
  data = data.slice(2);
  var f = 0;

  for (var i = 0; i < n; i ++) {
    var q = data[i].split(' ');

    if (q[0] == 1) {
      f ^= 1;

    } else {

      if (f ^ (q[1] - 1)) {
        res += q[2];

      } else {
        res = q[2] + res;

      }
    }
  }
  if (f) {
    res = res.split('').reverse().join('');
  }
  return res;
}

const input = require('fs').readFileSync('/dev/stdin', 'utf8').trim();
console.log(main(input));
