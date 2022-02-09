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


int main() {
  ios::sync_with_stdio(false); cin.tie(0);
  // ex1();
  // ex2();
  // ex3();
  // ex4();
  // ex5();
  // abc084a();
  // abc076a();
  abc074a();
  return 0;
}
