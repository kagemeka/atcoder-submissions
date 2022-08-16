#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  vector<vector<int>> g(m, vector<int>(m));
  for(int i = 0; i < m; i++) {
    for(int j = 0; j < m; j++) cin >> g[i][j];
  }
  vector<vector<int>> a(n, vector<int>(n));
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      int& x = a[i][j];
      cin >> x;
      x--;
    }
  }
  vector<vector<int>> cost(3, vector<int>(m));
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      int k = (i + j) % 3;
      int x = a[i][j];
      for(int y = 0; y < m; y++) { cost[k][y] += g[x][y]; }
    }
  }
  long const inf = 1l << 60;
  long mn = inf;
  for(int i = 0; i < m; i++) {
    for(int j = 0; j < m; j++) {
      if(i == j) continue;
      for(int k = 0; k < m; k++) {
        if(i == k || j == k) continue;
        mn = min(mn, (long)cost[0][i] + cost[1][j] + cost[2][k]);
      }
    }
  }
  cout << mn << '\n';
}