#include <bits/stdc++.h>
using namespace std;


class Solver {

string s;

void prepare() {
  cin >> s;
}


void solve() {
  if (s=="a") {
    cout << -1 << '\n';
  } else {
    cout << 'a' << '\n';
  }
}


public:

void run() {
  prepare();
  solve();
}

};


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int t = 1;
  while (t--) {
    Solver solver;
    solver.run();
  }

  return 0;
}
