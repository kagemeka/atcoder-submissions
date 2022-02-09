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

int main() {
  ios::sync_with_stdio(false); cin.tie(0);
  // ex1();
  // ex2();
  // ex3();
  // ex4();
  ex5();
  return 0;
}
