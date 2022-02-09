#include <bits/stdc++.h>
using namespace std;


class Solver {

int n;

void prepare() {
  cin >> n;
}


void solve() {
  string s = to_string(n);
  bool flg = {
    n%3 == 0 ||
    s.find('3') != string::npos
  };
  cout << (flg ? "YES" : "NO")
    << '\n';
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
