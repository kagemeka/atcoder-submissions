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



abstract class AddSemiGroup<T>
{
  T operator +(
    T other,
  );
}



abstract class AddMonoid<T>
implements AddSemiGroup<T>
{
  T addIdentity();
}



abstract class AddGroup<T>
implements AddMonoid<T>
{
  T operator -();
}



mixin Subtraction<
  T extends AddGroup<T>
>
{

  T operator -(
    T other,
  ) {
    var x = this as T;
    return x + -other;
  }

}



abstract class MulSemiGroup<T>
{
  T operator *(
    T other,
  );
}



abstract class MulMonoid<T>
implements MulSemiGroup<T>
{
  T mulIdentity();
}



abstract class MulGroup<T>
implements MulMonoid<T>
{
  T inv();
}



mixin Division<
  T extends MulGroup<T>
>
{
  T operator /(
    T other,
  ) {
    var x = this as T;
    return x * other.inv();
  }
}



mixin Power<
  T extends MulMonoid<T>
>
{


  T pow(
    int n,
  ) {
    var a = this as T;
    if (n == 0) {
      return a.mulIdentity();
    }
    var x = pow(n >> 1);
    x *= x;
    if (n & 1 == 1) x *= a;
    return x;
  }


}



abstract class Ring<T>
implements
AddGroup<T>,
MulMonoid<T>
{
}


abstract class Field<T>
implements
AddGroup<T>,
MulGroup<T>
{
}



extension
CumProd<
  T extends MulSemiGroup<T>
>
on List<T> {


  List<T> cumprod()
  {
    var a = List<T>.from(this);
    int n = a.length;
    for (
      int i = 0; i < n - 1; i++
    ) {
      a[i + 1] *= a[i];
    }
    return a;
  }


}



extension
CumSum<
  T extends AddSemiGroup<T>
>
on List<T> {


  List<T> cumpsum()
  {
    var a = List<T>.from(this);
    int n = a.length;
    for (
      int i = 0; i < n - 1; i++
    ) {
      a[i + 1] += a[i];
    }
    return a;
  }


}



class Modular
with
Power<Modular>,
Division<Modular>,
Subtraction<Modular>
implements
Field<Modular>
{


  int value = 0;
  final int mod;


  Modular(
    this.value,
    this.mod,
  ) {
    value %= mod;
  }


  Modular.define(this.mod);


  Modular call(
    int value,
  ) {
    return Modular(value, mod);
  }


  Modular operator +(
    final Modular other,
  ) {
    return Modular(
      value + other.value,
      mod,
    );
  }


  Modular addIdentity()
  {
    return Modular(0, mod);
  }


  Modular operator -() {
    return Modular(
      -value,
      mod,
    );
  }


  Modular operator *(
    Modular other,
  ) {
    return Modular(
      value * other.value,
      mod,
    );
  }


  Modular mulIdentity() {
    return Modular(1, mod);
  }


  Modular inv() {
    return this.pow(mod - 2);
  }


  String toString() {
    return '${value}';
  }


  List<Modular> factorial()
  {
    int n = value;
    List<Modular> a = [
      Modular(1, mod),
      for (
        int i = 1; i < n; i++
      ) Modular(i, mod)
    ];
    a = a.cumprod();
    return a;
  }


  List<Modular> invFactorial()
  {
    int n = value;
    var fac = this.factorial();
    List<Modular> a = [
      for (
        int i = n; i > 0; i--
      ) Modular(i, mod)
    ];
    a[0] = fac[n - 1].inv();
    a = a.cumprod();
    a = a.reversed.toList();
    return a;
  }


}



class Problem
with
Runner<Problem>,
IO
implements Solver
{

  final int mod = 1000000007;
  final mint = Modular.define(
    1000000007,
  );


  int
  n = 0,
  m = 0,
  k = 0;

  List<Modular> a = [];
  List<int> x = [], y = [];


  void prepare() {
    n = readInt();
    m = readInt();
    k = readInt();
    for (
      int i = 0; i < n; i++
    ) {
      a.add(mint(readInt()));
    }
    for (
      int i = 0; i < m; i++
    ) {
      x.add(readInt() - 1);
      y.add(readInt() - 1);
    }
  }


  void solve() {
    makeGraph();
    doubling();
    List<List<Modular>> a;
    a = toMatrix(this.a);
    a = dot(g, a);
    for (var x in a) {
      write(x[0]);
    }
  }


  List<List<Modular>>
  toMatrix(
    List<Modular> a,
  ) {
    List<List<Modular>> b;
    b = List.filled(n, []);
    for (
      int i = 0; i < n; i++
    ) b[i] = [a[i]];
    return b;
  }


  void doubling()
  {
    g = pow(g, k);
  }


  List<List<Modular>> g = [];


  void makeGraph()
  {
    g = List.filled(n, []);

    var v = mint(m * 2);
    for (
      int i = 0; i < n; i++
    ) {
      g[i] = List.filled(
        n,
        mint(0),
      );
      g[i][i] = v;
    }
    for (
      int i = 0; i < m; i++
    ) {
      var x = this.x[i];
      var y = this.y[i];
      g[x][x] -= mint(1);
      g[y][y] -= mint(1);
      g[x][y] += mint(1);
      g[y][x] += mint(1);
    }
    toProbability();
  }


  void toProbability() {
    var v = mint(m * 2).inv();
    for (
      int i = 0; i < n; i++
    ) {
      for (
        int j = 0; j < n; j++
      ) {
        g[i][j] *= v;
      }
    }
  }


  List<List<Modular>>
  pow(
    List<List<Modular>> a,
    int n,
  ) {
    if (n == 0) {
      return identity();
    }
    var x = pow(a, n >> 1);
    x = dot(x, x);
    if (n & 1 == 1) {
      x = dot(x, a);
    }
    return x;
  }


  List<List<Modular>>
  identity() {
    List<List<Modular>> e;
    e = List.filled(n, []);
    for (
      int i = 0; i < n; i++
    ) {
      e[i] = List.filled(
        n,
        mint(0),
      );
      e[i][i] = mint(1);
    }
    return e;
  }


  List<List<Modular>>
  dot(
    List<List<Modular>> a,
    List<List<Modular>> b,
  ) {
    List<List<Modular>> c;
    int n = a.length;
    int m = b[0].length;
    c = List.filled(n, []);
    for (
      int i = 0; i < n; i++
    ) {
      c[i] = List.filled(
        m,
        mint(0),
      );
    }
    for (
      int i = 0; i < n; i++
    ) {
      for (
        int j = 0; j < m; j++
      ) {
        dotSuppot(
          c, a, b, i, j,
        );
      }
    }
    return c;
  }


  void dotSuppot(
    List<List<Modular>> c,
    List<List<Modular>> a,
    List<List<Modular>> b,
    int i,
    int j,
  ) {
    var n = b.length;
    var x = mint(0);
    for (
      int k = 0; k < n; k++
    ) {
      x += a[i][k] * b[k][j];
    }
    c[i][j] = x;
  }

}



void main()
{
  var p = new Problem();
  p();
}
