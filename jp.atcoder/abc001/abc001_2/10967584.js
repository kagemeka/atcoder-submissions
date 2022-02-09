const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  var d = int(input) / 1000;
  var v;
  if (d < 0.1) {
    v = '00';
  } else {
    if (d <= 5) {
      v = (d * 10).toString(10);
      (d < 1) ? v = '0' + v : null;
    } else {
      if (d <= 30) {
        v = d + 50;
      } else {
        if (d <= 70) {
          v = (d - 30) / 5 + 80;
        } else {
          v = 89;
        }
      }
    }
  }
  console.log(v);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
