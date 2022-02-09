 const fs = require('fs');

function main(input) {
  var s = input.split('')
  var cnt = 0;
  for (var i = 0; i < 3; i++) {
    if (s[i] == '1') {
      cnt++
    }
  }
  console.log(cnt)
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
