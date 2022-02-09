import 'dart:io';
import 'dart:convert';



class Reader {


  List<int> buf = [];
  List<String> gen = [];
  int cnt = 0;


  Reader() {
    read();
  }


  int i() {
    return int.parse(s());
  }


  String s() {
    var s = gen[cnt];
    cnt++;
    return s;
  }


  int readByte() => (
    stdin
    .readByteSync()
  );


  read() {
    while (true) {
      var b = readByte();
      if (b == 4) break;
      if (
        b != 10 && b != 32
      ) {
        buf.add(b);
        continue;
      }
      if (
        buf.isEmpty
      ) continue;
      var s = utf8.decode(
        buf,
      );
      gen.add(s);
      buf = [];
    }
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


  Reader reader = new Reader();


  int h0 = 0;
  int h1 = 0;


  void prepare() {
    h0 = reader.i();
    h1 = reader.i();
  }


  void solve() {
    print(h0 - h1);
  }


}



void main() {
  stdin.lineMode = false;
  var p = new Problem();
  p();
}
