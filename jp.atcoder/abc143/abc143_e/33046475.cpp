
#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m, l;
  cin >> n >> m >> l;
  long const inf = 1l << 60;
  vector<vector<long>> g(n, vector<long>(n, inf));
  while(m--) {
    int a, b, c;
    cin >> a >> b >> c;
    a--;
    b--;
    g[a][b] = c;
    g[b][a] = c;
  }
  for(int i = 0; i < n; i++) g[i][i] = 0;
  auto floyd = [&]() {
    for(int k = 0; k < n; k++) {
      for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
          g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
        }
      }
    }
  };
  floyd();
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) { g[i][j] = g[i][j] <= l ? 1 : inf; }
  }
  floyd();
  int q;
  cin >> q;
  while(q--) {
    int s, t;
    cin >> s >> t;
    s--;
    t--;
    long d = g[s][t];
    cout << (d == inf ? -1 : d - 1) << endl;
  }
}
