const fs = require('fs');

function main(input) {
  var s = input.trim();
  var set = new Set(s);

  if (set.size == 1) {
    var res = 'No';
  } else {
    var res = 'Yes';
  }
  console.log(res);
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
