const fs = require('fs');

function main(input) {
  let s = input.split('')
  let cnt = 0;
  for (let i = 0; i < 3; i++) {
    if (s[i] == '1') {
      cnt++
    }
  }
  console.log(cnt)
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
