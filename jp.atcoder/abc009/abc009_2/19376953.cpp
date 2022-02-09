#include <bits/stdc++.h>
using namespace std;


class Solver {

private:

int n;
vector<int> a;

void prepare() {
  cin >> n;
  a = vector<int>(n);
  for (int i = 0; i < n; i++)
  {
    cin >> a[i];
  }
}


void solve() {
  auto s = set<int>(
    a.begin(), a.end()
  );
  auto it = s.end();
  advance(it, -2);
  cout << *it << '\n';
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
