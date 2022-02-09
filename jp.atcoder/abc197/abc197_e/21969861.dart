import 'dart:io';
import 'dart:convert';
import 'dart:math';



class IO
{


  int readByte() => (
    stdin
    .readByteSync()
  );


  String readLine() => (
    stdin
    .readLineSync()!
    .trim()
  );


  int readInt() => int.parse(
    read(),
  );


  List<String> buf = [];
  int i = 0;

  String read()
  {
    i++;
    if (i < buf.length)
    {
      return buf[i];
    }
    String l = readLine();
    buf = l.split(
      RegExp('\ |\n')
    );
    i = -1;
    return read();
  }



  // String read()
  // {
  //   List<int> bytes = [];
  //   // const int maxWait = 1 << 8;
  //   // int wait = 0;
  //   while (true)
  //   {
  //     var b = readByte();
  //     // if (
  //     //   wait == maxWait
  //     // ) break;
  //     // if (b == -1)
  //     // {
  //     //   wait++;
  //     //   continue;
  //     // }
  //     // wait = 0;
  //     if (
  //       b == 10 ||
  //       b == 32
  //     ) {
  //       break;
  //     }
  //     bytes.add(b);
  //   }
  //   var s = utf8.decode(bytes);
  //   return s;
  // }


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



class Item
implements Comparable<Item> {

  int x = 0;
  int c = 0;


  Item(this.x, this.c);


  @override
  int compareTo(
    Item other,
  ) {
    if (this.c != other.c) {
      return this.c - other.c;
    }
    return x - other.x;
  }


  String toString() {
    return '$x $c';
  }


}





class Problem
with
Runner<Problem>,
IO
implements Solver
{


  int n = 0;
  List<Item> items = [];


  void prepare() {
    n = readInt();
    for (
      int i = 0; i < n; i++
    ) {
      int x, c;

      x = readInt();
      c = readInt() - 1;
      var item = Item(x, c);
      items.add(item);
    }

  }


  void solve() {
    preprocess();
    write(dp());
  }


  List<List<int>> coords = [];
  List<List<int>> dist = [];
  int i = 0;


  int dp() {
    dist = [
      for (
        int i = 0; i < n; i++
      ) [0, 0]
    ];
    for (
      int i = 0; i < n - 1; i++
    ) {
      this.i = i;
      dpSupport();
    }
    return dist[n - 1][0];
  }


  void dpSupport() {
    List<int> from, to;
    from = coords[i];
    to = coords[i + 1];
    int delta = to[1] - to[0];
    List<int> d = dist[i];
    List<int> tmp = [0, 0];
    for (
      int i = 0; i < 2; i++
    ) {
      int y = to[i];
      int x0 = from[0];
      int x1 = from[1];
      tmp[i] = min(
        d[0] + (y - x0).abs(),
        d[1] + (y - x1).abs(),
      );
    }
    d[0] = tmp[1] + delta;
    d[1] = tmp[0] + delta;
    dist[i + 1] = d;
  }


  void preprocess() {
    items.sort();
    List<int> coords, ids;
    coords = List.filled(n, 0);
    ids = List.filled(n, 0);
    for (
      int i = 0; i < n; i++
    ) {
      var item = items[i];
      coords[i] = item.x;
      ids[i] = item.c;
    }
    List<List<int>> a;
    a = [[0, 0]];
    for (
      int i = 0; i < n; i++
    ) {
      int l, r;
      l = ids.bisectLeft(i);
      r = ids.bisectRight(i);
      if (l == r) continue;
      l = coords[l];
      r = coords[r - 1];
      a.add([l, r]);
    }
    a.add([0, 0]);
    this.coords = a;
    n = a.length;
  }


}


extension Bisect<E> on List<E> {


  int bisectLeft(
    E element,
  ) {
    int lo = 0, hi = length;
    var compare = (
      Comparable.compare
      as Function(E, E)
    );
    while (lo < hi) {
      var x = (lo + hi) ~/ 2;
      if (
        compare(
          element,
          this[x],
        ) > 0
      ) {
        lo = x + 1;
      } else {
        hi = x;
      }
    }
    return lo;
  }


  int bisectRight(
    E element,
  ) {
    int lo = 0, hi = length;
    var compare = (
      Comparable.compare
      as Function(E, E)
    );
    while (lo < hi) {
      var x = (lo + hi) ~/ 2;
      if (
        compare(
          element,
          this[x],
        ) < 0
      ) {
        hi = x;
      } else {
        lo = x + 1;
      }
    }
    return lo;
  }


}



void main() {
  var p = new Problem();
  p();

}
