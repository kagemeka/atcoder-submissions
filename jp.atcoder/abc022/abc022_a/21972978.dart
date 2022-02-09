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

  int n = 0;
  int s = 0;
  int t = 0;
  List<int> a = [];

  void prepare() {
    n = readInt();
    s = readInt();
    t = readInt();
    a = [
      for (
        int i = 0; i < n; i++
      ) readInt()
    ];
  }


  void solve() {
    for (
      int i = 0; i < n - 1; i++
    ) a[i + 1] += a[i];
    int tot = 0;
    for (int x in a)
    {
      if (x < s || x > t)
      {
        continue;
      }
      tot++;
    }
    write(tot);
  }


}



void main()
{
  var p = new Problem();
  p();
}
