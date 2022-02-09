#include <bits/stdc++.h>

using namespace std;

void ex1() {
  cout << "こんにちは" << '\n' << "AtCoder" << '\n';
}

void ex2() {
  cout << "いつも2525\nAtCoderくん" << '\n';
}

void ex3() {
  int a = 101*100/2;
  cout << a << '\n';
}

void ex4() {
  vector<int> a = {1, 2, 5, 10};
  int s = 365*24*60*60;
  for (auto &x: a) {
    cout << x*s << '\n';
  }
}

void ex5() {
  int a, b; cin >> a >> b;
  cout << a+b << '\n';

}


void abc084a() {
  int m; cin >> m;
  cout << 48-m << '\n';
}

void abc076a() {
  int r, g;
  cin >> r >> g;
  cout << 2*g - r << '\n';
}

void abc074a() {
  int n, a;
  cin >> n >> a ;
  cout << n*n - a << '\n';

}

void abc082a() {
  int a, b ;
  cin >> a >> b;
  cout << (a+b+1)/2 << '\n';
}

void abc081a() {
  char c;
  int tot = 0;
  for (int i = 0; i < 3; i++) {
    cin >> c;
    tot += c-'0';
  }
  cout << tot << '\n';

}

void ex6() {
  int a, b; char op;
  cin >> a >> op >> b;
  int res;

  switch (op) {
    case '+': res = a+b; break;
    case '-': res = a-b; break;
    case '*': res = a*b; break;
    case '/': if (!b) {cout << "error" << '\n'; return;}
              res = a/b; break;
    default : cout << "error" << '\n'; return;

  }
  cout << res << '\n';
}

void abc088a() {
  int n, a;
  cin >> n >> a;
  string ans = "No";
  if (n%500 <= a) {ans = "Yes";}
  cout << ans << '\n';

}


void abc086a() {
  int a, b; cin >> a >> b;
  string ans = "Even";
  if (a*b&1) {ans = "Odd";}
  cout << ans << '\n';
}

void abc083a() {
  int a, b, c, d, l, r;
  cin >> a >> b >> c >> d;
  l = a+b, r = c+d;
  string ans = l>r? "Left" : (l==r? "Balanced" : "Right");
  cout << ans << '\n';
}

void abc080a() {
  int a, b, c;
  cin >> a >> b >> c;
  cout << min(a*b, c) << '\n';
}

void abc079a() {
  string a; cin >> a;
  string ans = (a[1]==a[2] && (a[0]==a[1] || a[2]==a[3]))? "Yes" : "No";
  cout << ans << '\n';
}

void ex8() {
  int f, p, n; string t;
  cin >> f;
  if (f==1) {
    cin >> p >> n;
    cout << p*n << '\n';
  } else {
    cin >> t >> p >> n;
    cout << t+'!' << '\n';
    cout << p*n << '\n';
  }
}

void ex9() {
  int x, a, b;
  cin >> x >> a >> b;
  cout << ++x << '\n';
  x *= a+b; cout << x << '\n';
  x *= x; cout << x << '\n';
  cout << --x << '\n';
}


string repeat(string s, int n) {
  string t;
  while (n) {
    if (n&1) t += s;
    s += s; n >>= 1;
  }
  return t;
}



void ex10() {
  int a, b; cin >> a >> b;
  cout << "A:" + repeat("]", a) << '\n';
  cout << "B:" + repeat("]", b) << '\n';
}

void ex11() {
  int n, a; cin >> n >> a;
  for (int i = 0; i < n; i++) {
    char op; int b; cin >> op >> b;
    switch (op) {
      case '+': a += b; break;
      case '-': a -= b; break;
      case '*': a *= b; break;
      case '/': if (!b) {cout << "error" << '\n'; return;}
                a /= b; break;

    }
    cout << i+1 << ':' << a << '\n';
  }
}

void abc089b() {
  int n; cin >> n;
  unordered_set<char> s;
  for (int i = 0; i < n; i++) {
    char c; cin >> c;
    s.insert(c);
  }
  string ans = s.size()==3? "Three" : "Four";
  cout << ans << '\n';

}

void abc073b() {
  int n; cin >> n;
  int tot = 0;
  for (int i = 0; i < n; i++) {
    int l, r;
    cin >> l >> r;
    tot += r-l + 1;
  }
  cout << tot << '\n';
}

void abc080b() {
  auto is_harshad = [](int x) {
    int s = 0;
    int y = x;
    while (x) {
      s += x%10;
      x /= 10;
    }
    return y%s == 0;
  };
  int x; cin >> x;
  string ans = is_harshad(x)? "Yes" : "No";
  cout << ans << '\n';


}

int main() {
  ios::sync_with_stdio(false); cin.tie(0);
  // ex1();
  // ex2();
  // ex3();
  // ex4();
  // ex5();
  // abc084a();
  // abc076a();
  // abc074a();
  // abc082a();
  // abc081a();
  // ex6();
  // abc088a();
  // abc086a();
  // abc083a();
  // abc080a();
  // abc079a();
  // ex8();
  // ex9();
  // ex10();
  // ex11();
  // abc089b();
  // abc073b();
  abc080b();
  return 0;

}
