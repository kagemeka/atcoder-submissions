#include <bits/stdc++.h>
using namespace std;


class Solver {

int n;
vector<int> t;
const int mod = 10007;


void prepare() {
  cin >> n;
  n--;
  t = vector<int>(n + 1);
  t[0] = 0;
  t[1] = 0;
  t[2] = 1;
}


void solve() {
  for (int i = 3; i < n+1; i++)
  {
    t[i] = t[i-1] + t[i-2]
      + t[i-3];
    t[i] %= mod;
  }
  cout << t[n] << '\n';
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
