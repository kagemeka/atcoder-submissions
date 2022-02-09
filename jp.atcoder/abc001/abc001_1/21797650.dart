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


  IO io = new IO();


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
    h0 = io.readInt();
    h1 = io.readInt();
  }


  void solve() {
    print(h0 - h1);
  }


}



void main() {
  var p = new Problem();
  p();
}
