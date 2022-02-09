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


  String n = '';


  void prepare() {
    n = read();
  }


  void solve() {
    bool b1 = n.contains('3');
    int d = int.parse(n);
    bool b2 = d % 3 == 0;
    bool ok = b1 || b2;
    String ans = (
      ok ? 'YES' : 'NO'
    );
    print(ans);
  }


}



void main() {
  var p = new Problem();
  p();
}
