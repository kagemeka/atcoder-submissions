'use strict';


class IO {
  fs: any = require(
    'fs',
  )
  chunks: Generator;
  readStdin(): (
    string
  ) {
    const fs: any = this.fs
    return fs.readFileSync(
      '/dev/stdin',
      'utf8',
    );
  }
  toChunks(s: string): (
    string[]
  ) {
    return (
      s.trim().split(/ |\n/)
    );
  }

  *toGen(chunks: string[]): (
    Generator
  ) {
    for (var c of chunks) {
      yield c;
    }
  }

  constructor() {
    const fs = this.fs;
    const chunks: (
      string[]
    ) = this.toChunks(
      this.readStdin(),
    );
    this.chunks = this.toGen(
      chunks,
    );
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
