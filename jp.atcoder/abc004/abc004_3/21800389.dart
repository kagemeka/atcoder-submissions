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


  int n = 0;
  final int m = 6;
  List<int> a = [];


  void prepare() {
    n = readInt();
    a = List.filled(m, 0);
    for (
      int i = 0; i < m; i++
    ) a[i] = i % m + 1;
  }


  void solve() {
    n %= m * (m - 1);
    a += a;
    int r = n % (m - 1);
    n ~/= m - 1;
    a = a.sublist(n, n + m);
    swap(r);
    for (
      int x in a
    ) stdout.write(x);
    stdout.writeln();
  }


  void swap(
    int n,
  ) {
    for (
      int i = 0; i < n; i++
    ) {
      int tmp;
      tmp = a[i];
      a[i] = a[i + 1];
      a[i + 1] = tmp;
    }
  }


}



void main() {
  var p = new Problem();
  p();
}
