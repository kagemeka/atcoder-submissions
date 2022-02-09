import 'dart:io';



String read() => (
  stdin
  .readLineSync()
  .trim()
);


int readInt() => (
  int.parse(read())
);




class Solver {
  prepare() {}

  solve() {}
}


mixin Runner {
  prepare() {}

  solve() {}

  call() {
    prepare();
    solve();
  }
}



class Problem
with Runner
implements Solver {
  int h0 = 0;
  int h1 = 0;
  prepare() {
    this.h0 = readInt();
    this.h1 = readInt();
  }
  solve() {
    var h0 = this.h0;
    var h1 = this.h1;
    print(h0 - h1);
  }
}



void main() {
  var p = new Problem();
  p();
}
