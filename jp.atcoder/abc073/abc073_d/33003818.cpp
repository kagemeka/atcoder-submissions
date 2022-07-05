#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, m, k;
  cin >> n >> m >> k;
  vector<int> r(k);
  for(int i = 0; i < k; i++) cin >> r[i];
  int const inf = 1 << 29;
  vector<vector<int>> g(n, vector<int>(n, inf));
  while(m--) {
    int a, b, c;
    cin >> a >> b >> c;
    a--;
    b--;
    g[a][b] = c;
    g[b][a] = c;
  }
  for(int i = 0; i < n; i++) { g[i][i] = 0; }
  for(int k = 0; k < n; k++) {
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < n; j++) { g[i][j] = min(g[i][j], g[i][k] + g[k][j]); }
    }
  }

  int mn = inf;
  vector<int> range(k);
  iota(range.begin(), range.end(), 0);
  do {
    int d = 0;
    for(int i = 0; i < k - 1; i++) {
      int a = r[range[i]] - 1, b = r[range[i + 1]] - 1;
      d += g[a][b];
    }
    mn = min(mn, d);
  } while(next_permutation(range.begin(), range.end()));
  cout << mn << endl;
}
