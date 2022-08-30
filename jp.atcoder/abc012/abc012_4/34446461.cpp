#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for(int i = 0; i < n; i++)
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  int const inf = 1 << 29;
  vector<vector<int>> g(n, vector<int>(n, inf));
  for(int i = 0; i < n; i++) g[i][i] = 0;
  while(m--) {
    int a, b, t;
    cin >> a >> b >> t;
    a--;
    b--;
    g[a][b] = g[b][a] = t;
  }
  rep(k, n) rep(i, n) rep(j, n) g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
  int res = inf;
  for(auto& d: g) { res = min(res, *max_element(d.begin(), d.end())); }
  cout << res << endl;
}
