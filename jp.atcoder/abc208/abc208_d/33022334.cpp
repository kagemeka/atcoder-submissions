#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, m;
  cin >> n >> m;

  int const inf = 1 << 29;
  vector<vector<int>> g(n, vector<int>(n, inf));
  for(int i = 0; i < m; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    a--;
    b--;
    g[a][b] = c;
  }
  for(int i = 0; i < n; i++) g[i][i] = 0;

  long tot = 0;
  for(int k = 0; k < n; k++) {
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < n; j++) {
        g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
        if(g[i][j] != inf) tot += g[i][j];
      }
    }
  }
  cout << tot << endl;
}