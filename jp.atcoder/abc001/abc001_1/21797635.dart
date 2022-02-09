import 'dart:io';
import 'dart:convert';



class IO {


  int readByte() => (
    stdin
    .readByteSync()
  );


  int read_int() {
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
with Runner {


  IO io = new IO();


  int h0 = 0;
  int h1 = 0;


  void prepare() {
    h0 = io.read_int();
    h1 = io.read_int();
  }


  void solve() {
    print(h0 - h1);
  }


}



void main() {
  var p = new Problem();
  p();
}
