import 'dart:io';
import 'dart:convert';
import 'dart:math';



class IO {


  int readByte() => (
    stdin
    .readByteSync()
  );


  int readInt() => int.parse(
    read(),
  );


  String read() {
    List<int> bytes = [];
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


  void write(
    dynamic object,
  ) {
    stdout.write(object);
    stdout.writeln();
  }


  void writeIter(
    Iterable<dynamic> objects,
  ) {
    stdout.writeAll(
      objects,
      ' ',
    );
    stdout.writeln();
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


  int n = 0, k = 0;
  List<int> r = [];


  void prepare() {
    n = readInt();
    k = readInt();
    r = List.filled(n, 0);
    for (
      int i = 0; i < n; i++
    ) r[i] = readInt();
  }


  void solve() {
    r.sort(
      (x, y) => y - x,
    );
    double rate = 0;
    for (
      int i = k - 1;
      i > -1;
      i--
    ) {
      rate = (rate + r[i]) / 2;
    }
    write(rate);
  }


}



void main() {
  var p = new Problem();
  p();
}
