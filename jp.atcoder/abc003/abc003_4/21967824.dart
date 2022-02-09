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




extension
CumProd<
  T extends MulSemiGroup
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
CumSum<T extends AddSemiGroup>
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



class ModChoose<T>
{


  List<Modular>
  fac = [],
  iFac = [];


  ModChoose(
    Modular n,
  ) {
    fac = n.factorial();
    iFac = n.invFactorial();
  }


  Modular call(
    int n,
    int r,
  ) {
    if (r > n || r < 0)
    {
      return (
        fac[0].addIdentity()
      );
    }
    var res;
    res = fac[n];
    res *= iFac[r];
    res *= iFac[n - r];
    return res;
  }


}





class Problem
with
Runner<Problem>,
IO
implements Solver
{


  final mint = Modular.define(
    1000000007,
  );

  int
  r = 0,
  c = 0,
  x = 0,
  y = 0,
  d = 0,
  l = 0;


  void prepare()
  {
    r = readInt();
    c = readInt();
    y = readInt();
    x = readInt();
    d = readInt();
    l = readInt();
  }


  var choose;


  void solve()
  {
    const int mx = 1 << 10;
    choose = ModChoose(
      mint(mx),
    );
    write(countUp());
  }


  int i = 0;
  List<int> cnt = [];
  final int n = 4;


  Modular countUp()
  {
    var a = mint(-1);
    var s = mint(0);
    for (
      int i = 0;
      i < 1 << n;
      i++
    ) {
      cnt = [0, 0];
      this.i = i;
      countSupport();
      Modular c;
      c = a.pow(i.bitCount);
      c *= chooseSupport(
        y - cnt[0],
        x - cnt[1],
      );
      s += c;
    }
    int blocks;
    blocks = r - y + 1;
    blocks *= c - x + 1;
    s *= mint(blocks);
    s *= choose(d + l, d);
    return s;
  }


  Modular chooseSupport(
    int y,
    int x,
  ) {
    if (y < 0 || x < 0)
    {
      return mint(0);
    }
    return choose(
      y * x,
      d + l,
    );
  }


  void countSupport()
  {
    for (
      int j = 0; j < n; j++
    ) {
      if (~i >> j & 1 == 1)
      {
        continue;
      }
      cnt[j & 1]++;
    }
  }


}



extension BitCount on int
{


  int get bitCount
  {
    int n = this;
    int cnt = 0;
    while (n > 0)
    {
      cnt += n & 1;
      n >>= 1;
    }
    return cnt;
  }


}




void main()
{
  var p = new Problem();
  p();
}
