import 'dart:io';
import 'dart:convert';



class IO {


  int readByte() => (
    stdin
    .readByteSync()
  );


  int readInt() {
    var s = read();
    return int.parse(s);
  }


  String read() {
    List<int>  bytes = [];
    while (true) {
      var b = readByte();
      if (
        b == 10 || b == 32
      ) {
        break;
      }
      bytes.add(b);
    }
    var s = utf8.decode(bytes);
    return s;
  }


}



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
extends IO
with Runner {


  int n = 0;


  void prepare() {
    n = readInt();
  }


  void solve() {
    print(--n);
  }


}



void main() {
  var p = new Problem();
  p();
}
