const fs = require('fs');

function main(input) {
  arr = input.split('\n');
  var a = parseInt(arr[0]);
  var b = parseInt(arr[1]);
  var c = parseInt(arr[2]);
  var x = parseInt(arr[3]) / 50;

  var tot;
  var cnt = 0;
  for (var i = 0; i <= a; i++) {
    for (var j = 0; j <=  b; j++) {
      for (var k = 0; k <= c; k++) {
        tot = 10*i + 2*j + k;
        if (tot === x) {
          cnt++
        }
      }
    }
  }
  console.log(cnt)
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
