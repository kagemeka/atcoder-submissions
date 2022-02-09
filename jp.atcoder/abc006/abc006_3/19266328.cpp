#include <bits/stdc++.h>
using namespace std;


class Solver {

int n, m;

void prepare() {
  cin >> n >> m;
}


void solve() {
  int a = 0, b = 0, c = 0;
  if (m&1) {
    m -= 3;
    n -= 1;
    b++;
  }
  c = m / 2 - n;
  a = n - c;
  if (a<0 || b<0 || c<0) {
    a = b = c = -1;
  }
  cout << a << ' ' << b << ' '
    << c << '\n';
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
