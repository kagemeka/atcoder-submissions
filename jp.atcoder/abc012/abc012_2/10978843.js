const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function divmod(a, b) {
  var q, r;
  q = Math.floor(a / b);
  r = a % b;
  return [q, r];
}

function toS(i) {
  return (i < 10) ?  '0' + i.toString(10) : i.toString(10);
}

function main(input) {
  var n = int(input.trim());
  var h, m, s;
  var d;
  d = divmod(n, 3600);
  h = d[0];
  n = d[1];
  d = divmod(n, 60);
  m = d[0];
  s = d[1];
  h = toS(h);
  m = toS(m);
  s = toS(s);
  var res = `${h}:${m}:${s}`;
  console.log(res);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
