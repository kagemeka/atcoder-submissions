import 'dart:io';
import 'dart:convert';
import 'dart:math';



class IO
{


  int readByte() => (
    stdin
    .readByteSync()
  );


  int readInt() => int.parse(
    read(),
  );


  String read()
  {
    List<int> bytes = [];
    const int maxWait = 1 << 8;
    int wait = 0;
    while (true)
    {
      var b = readByte();
      if (
        wait == maxWait
      ) break;
      if (b == -1)
      {
        wait++;
        continue;
      }
      wait = 0;
      if (
        b == 10 ||
        b == 32
      ) {
        break;
      }
      bytes.add(b);
    }
    var s = utf8.decode(bytes);
    return s;
  }


  void write(
    Object object,
  ) {
    stdout.write(object);
    stdout.writeln();
  }


  void writeIter(
    Iterable<Object> objects,
    {
      String sep = ' ',
    }
  ) {
    stdout.writeAll(
      objects,
      sep,
    );
    stdout.writeln();
  }


}



abstract class Solver
{


  void prepare() {}


  void solve() {}


}



mixin Runner<
  T extends Solver
>
{


  void call() {
    var sol = this as T;
    sol.prepare();
    sol.solve();
  }


}



class Problem
with
Runner<Problem>,
IO
implements Solver
{


  final int n = 3;
  List<List<int>> a = [];


  void prepare() {
    for (
      int i = 0; i < n; i++
    ) {
      int x;
      x = readInt();
      a.add([i, x]);
    }
  }


  void solve() {
    a.sort(
      (x, y) {
        return y[1] - x[1];
      },
    );
    List<int> res = [];
    res = List.filled(n, 0);
    for (
      int i = 0; i < n; i++
    ) {
      res[a[i][0]] = i + 1;
    }
    for (
      var x in res
    ) {
      write(x);
    }
  }


}



void main()
{
  var p = new Problem();
  p();
}
