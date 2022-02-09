const fs = require('fs');

function main(input) {
  var input = input.split(' ');
  var a = parseInt(input[0])
  var b = parseInt(input[1])
  var ans = ""
  if (a * b & 1) {
    ans = 'Odd'
  } else {
    ans = 'Even'
  }
  console.log(ans);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
