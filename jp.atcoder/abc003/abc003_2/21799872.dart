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


  String s = '', t = '';
  Set<int> atcoder = (
    'atcoder'.runes.toSet()
  );
  int wildcard = (
    '@'.codeUnitAt(0)
  );

  int i = 0;


  void prepare() {
    s = read();
    t = read();
  }


  void solve() {
    int n = s.length;
    for (
      int i = 0; i < n; i++
    ) {
      this.i = i;
      if (
        check()
      ) continue;
      write('You will lose');
      return;
    }
    write('You can win');
  }


  bool check() {
    int x, y;
    x = s.codeUnitAt(i);
    y = t.codeUnitAt(i);
    if (x == y) return true;
    if (
      x == wildcard &&
      atcoder.contains(y)
    ) return true;
    if (
      y == wildcard &&
      atcoder.contains(x)
    ) return true;
    return false;
  }


}



void main() {
  var p = new Problem();
  p();
}
