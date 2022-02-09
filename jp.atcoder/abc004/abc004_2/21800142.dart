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


  List<List<String>> c = [];
  final int n = 4;
  int i = 0;


  void prepare() {
    c = List.filled(n, []);
    for (
      int i = 0; i < n; i++
    ) {
      this.i = i;
      readLine();
    }
  }


  void readLine() {
    List<String> row;
    row = List.filled(n, '');
    for (
      int j = 0; j < n; j++
    ) {
      row[j] = read();
    }
    c[i] = row;
  }


  void solve() {
    for (
      var row in c.reversed
    ) {
      writeIter(
        row.reversed,
      );
    }
  }


}



void main() {
  var p = new Problem();
  p();
}
