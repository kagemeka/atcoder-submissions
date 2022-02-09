'use strict';



class IO {

  private fs: (
    any
  ) = require(
    'fs',
  )

  chunks: Generator;


  private readStdin(): (
    string
  ) {
    const fs = this.fs
    return fs.readFileSync(
      '/dev/stdin',
      'utf8',
    );
  }


  private toChunks(
    s: string,
  ): (
    string[]
  ) {
    return (
      s.trim().split(/ |\n/)
    );
  }


  private *toGen(
    chunks: string[],
  ): (
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
  }


  read() {
    return (
      this.chunks.next().value
    );
  }


  readInt() {
    return +this.read();
  }
}



abstract class Solver {

  io: IO;


  constructor() {
    this.io = new IO();
  }


  abstract prepare()


  abstract solve()


  run() {
    this.prepare();
    this.solve();
  }
}



class ABC001A
extends Solver {

  h1: number;

  h2: number;


  prepare() {
    const io = this.io;
    const h1: (
      number
    ) = io.readInt();
    const h2: (
      number
    ) = io.readInt();
    this.h1 = h1;
    this.h2 = h2;
  }


  solve() {
    const h1 = this.h1;
    const h2 = this.h2;
    const d: number = h1 - h2;
    console.log(d);
  }
}



function main() {
  new ABC001A().run();
}


main()
