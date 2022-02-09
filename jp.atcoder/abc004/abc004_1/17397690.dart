import 'dart:io';
import 'dart:math';
import 'dart:convert';
import 'dart:async';


String read() => stdin.readLineSync();
int readInt() => int.parse(stdin.readLineSync());
List<String> readList() => stdin.readLineSync().split(' ');
List<int> readIntList() => (stdin.readLineSync().split(' ').map((x) => int.parse(x)).toList());

class ABC001 {
  static void a() {
    int h1 = readInt(), h2 = readInt();

    print(h1-h2);
  }

  static void b() {

  }
}


class ABC002 {
  static void a() {
    var l = readIntList();
    print(max(l[0], l[1]));
  }

  static void b() {
    Set<String> vowels = {'a', 'e', 'i', 'o', 'u'};
    String s = read();
    String t = '';
    for (var i = 0; i < s.length; i++) {
      if (vowels.contains(s[i])) continue;
      t += s[i];
    }
    print(t);
  }

  static void c() {

  }

  static void d() {
    int n, m;
    var l = readIntList();
    n = l[0]; m = l[1];
    List<int> relations = [for (int i = 0; i < n; i++) 0];
    for (int i = 0; i < m; i++) {
      l = readIntList();
      int x, y;
      x = l[0]-1; y = l[1]-1;
      relations[x] |= 1<<y; relations[y] |= 1<<x;
    }
    int res = 0;
    for (int i = 0; i < 1<<n; i++) {
      int s = (1<<n)-1, cnt=0;
      for (int j = 0; j < n; j++) {
        if (i>>j&1==1) {s &= relations[j] | 1<<j; cnt++;}
      }
      if (s&i==i) {res = max(res, cnt);}
    }
    print(res);
  }


}



class ABC003 {
  static void a() async {
    int n = readInt();
    print((1+n)*5000);

  }

  static void b() {
    var atcoder = {'a', 't', 'c', 'o', 'd', 'e', 'r'};

    String s, t;
    s = read(); t = read();

    for (int i = 0; i < s.length; i++) {
      if (s[i]==t[i]) continue;
      if (s[i]=='@' && atcoder.contains(t[i])) continue;
      if (t[i]=='@' && atcoder.contains(s[i])) continue;
      print('You will lose'); return;
    }
    print('You can win');
  }

  static void c() {
    List<int> il = readIntList();
    int n, k; n = il[0]; k = il[1];

    List<int> r = readIntList();
    r.sort((a,b) => b-a);

    double res = .0;
    for (int i = k-1; i > -1; i--) {
      res = (res+r[i])/2;
    }
    print(res);

  }

  static void d() {

  }
}

class ABC004 {
  static void a() {
    int n = readInt();
    print(n*2);
  }
}


void main() {
  ABC004.a();
}
