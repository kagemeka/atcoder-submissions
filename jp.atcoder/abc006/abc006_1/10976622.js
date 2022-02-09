const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  var n = int(input.trim());
  var ans = 'NO';
  if (n % 3 === 0) {
    ans = 'YES';
  } else {
    var digits = new Set(n.toString(10));
    if (digits.has('3')) {
      ans = 'YES'
    }
  }
  console.log(ans);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
