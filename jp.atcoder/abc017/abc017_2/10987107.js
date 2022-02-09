const fs = require('fs');

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  const tail = new Set('ch, o, k, u'.split(', '))
  var s = input.trim();
  while (s !== '') {
    l = s.length;
    if (tail.has(s.slice(-1))) {
      s = s.slice(0, -1);
      continue;
    } else {
      if (tail.has(s.slice(-2))) {
        s = s.slice(0, -2);
        continue;
      }
    }
    console.log('NO');
    return;
  }
  console.log('YES');
}

input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
