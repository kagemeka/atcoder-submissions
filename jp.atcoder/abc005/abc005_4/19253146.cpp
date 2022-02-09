#include <bits/stdc++.h>
using namespace std;

class Solver {

int n;
vector<vector<int>> d;
vector<int> s;


void prepare() {
  cin >> n;
  d = vector<vector<int>>(
    n + 1,
    vector<int>(n + 1)
  );
  for (
    int i = 1; i < n+1; i++
  ) {
    for (
      int j = 1; j < n+1; j++
    ) {
      cin >> d[i][j];
    }
  }
  s = vector<int>(n*n + 1);
}


void cumsum() {
  for (
    int i = 1; i < n+1; i++
  ) {
    for (
      int j = 1; j < n; j++
    ) {
      d[i][j+1] += d[i][j];
    }
  }
  for (
    int j = 1; j < n+1; j++
  ) {
    for (
      int i = 1; i < n; i++
    ) {
      d[i+1][j] += d[i][j];
    }
  }
}


void calc_concrete_yx(
  int y, int x
) {
  for (
    int i = y; i < n+1; i++
  ) {
    for (
      int j = x; j < n+1; j++
    ) {
      int k = (i-y+1) * (j-x+1);
      s[k] = max(
        s[k],
        d[i][j]
          - d[i][x-1]
          - d[y-1][j]
          + d[y-1][x-1]
      );
    }
  }
}


void query(int p) {
  cout << s[p] << '\n';
}


void solve() {
  cumsum();
  for (
    int y = 1; y < n+1; y++
  ) {
    for (
      int x = 1; x < n+1; x++
    ) {
      calc_concrete_yx(y, x);
    }
  }
  for (int i = 0; i < n*n; i++)
  {
    s[i+1] = max(s[i+1], s[i]);
  }
  int q;
  cin >> q;
  while (q--) {
    int p;
    cin >> p;
    query(p);
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
