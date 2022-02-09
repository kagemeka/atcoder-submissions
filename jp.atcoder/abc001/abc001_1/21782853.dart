import 'dart:io';



String read() => (
  stdin
  .readLineSync()
  .trim()
);


int readInt() => (
  int.parse(read())
);



abstract class Solver {


  void prepare() {}


  void solve() {}


}



mixin Runner
implements Solver {


  void call() {
    prepare();
    solve();
  }
}



class Problem
with Runner {


  int h0 = 0;
  int h1 = 0;


  void prepare() {
    this.h0 = readInt();
    this.h1 = readInt();
  }


  void solve() {
    var h0 = this.h0;
    var h1 = this.h1;
    print(h0 - h1);
  }
}



void main() {
  var p = new Problem();
  p();
}
