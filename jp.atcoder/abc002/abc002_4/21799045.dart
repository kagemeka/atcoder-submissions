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


  int n = 0, m = 0;
  List<int> x = [], y = [];

  List<int> rel = [];
  int s = 0;


  void prepare() {
    n = readInt();
    m = readInt();
    for (
      int i = 0; i < m; i++
    ) {
      int x, y;
      x = readInt() - 1;
      y = readInt() - 1;
      this.x.add(x);
      this.y.add(y);
    }
  }


  void solve() {
    makeRelations();
    int m = 1 << n;
    int mx = 0;
    for (
      int s = 0; s < m; s++
    ) {
      this.s = s;
      if (
        !checkIntersection()
      ) continue;
      mx = max(
        mx,
        bitCount(s),
      );
    }
    write(mx);
  }


  bool checkIntersection() {
    int t = s;
    for (
      int i = 0; i < n; i++
    ) {
      if (
        ~s >> i & 1 == 1
      ) continue;
      t &= rel[i];
    }
    return t == s;
  }


  void makeRelations() {
    rel = List.filled(n, 0);
    for (
      int i = 0; i < n; i++
    ) rel[i] |= 1 << i;

    for (
      int i = 0; i < m; i++
    ) {
      int x, y;
      x = this.x[i];
      y = this.y[i];
      rel[x] |= 1 << y;
      rel[y] |= 1 << x;
    }
  }


}



int bitCount(
  int n,
) {
  int cnt = 0;
  do {
    cnt += n & 1;
    n >>= 1;
  } while (
    n > 0
  );
  return cnt;
}



void main() {
  var p = new Problem();
  p();
}
