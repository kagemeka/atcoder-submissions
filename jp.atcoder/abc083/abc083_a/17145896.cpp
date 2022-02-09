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
  abc083a();
  return 0;

}
