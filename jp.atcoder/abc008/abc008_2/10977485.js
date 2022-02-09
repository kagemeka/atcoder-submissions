const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function counter(arr) {
  var cnt = {}
  arr.forEach(v => {
    cnt[v] = (cnt[v] || 0) + 1;
  });
  return cnt;
}

function main(input) {
  input = input.trim().split('\n');
  var s = input.slice(1);
  var cnt = counter(s);
  var max = 0;
  var res;
  s.forEach(s => {
    if (cnt[s] > max) {
      max = cnt[s];
      res = s;
    }
  });
  console.log(res);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
