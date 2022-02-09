'use strict';


class IO {
  fs = require(
    'fs'
  );
  chunks;
  constructor() {
    const fs = this.fs
    var i = fs.readFileSync(
      '/dev/stdin',
      'utf8',
    );
    this.chunks = function*() {
      i = i.trim().split(
        / |\n/,
      )
      for (var c of i) {
        yield c;
      }
    }();

  };
  read() {
    return (
      this.chunks.next().value
    );
  };
  readInt() {
    return +this.read();
  }
}

const io = new IO();

var h1: number;
var h2: number;
h1 = io.readInt();
h2 = io.readInt();
console.log(h1 - h2);
