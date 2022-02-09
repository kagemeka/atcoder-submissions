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


  int s = 0, t = 0;


  void prepare() {
    s = readInt();
    t = readInt();
  }


  void solve() {
    print(t - s + 1);
  }


}



void main() {
  var p = new Problem();
  p();
}
