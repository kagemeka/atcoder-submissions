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


  String w = '';
  Set<int> vowels = (
    'aeiou'.runes.toSet()
  );


  void prepare() {
    w = read();
  }


  void solve() {
    String s = '';
    for (
      int c in w.runes
    ) {
      if (
        vowels.contains(c)
      ) continue;
      s += String.fromCharCode(
        c,
      );
    }
    write(s);
  }


}



void main() {
  var p = new Problem();
  p();
}
