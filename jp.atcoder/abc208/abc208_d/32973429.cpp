#include <bits/stdc++.h>

using namespace std;

template <typename G, typename F>
auto floyd_warshall(G g, F f) -> G {
  int n = g.size();
  for (int k = 0; k < n; ++k) {
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        g[i][j] = f(g[i][j], g[i][k], g[k][j]);
      }
    }
  }
  return g;
}

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, m;
  cin >> n >> m;

  long inf = 1l << 60;
  vector<vector<long>> g(n, vector<long>(n, inf));
  while (m--) {
    int s, t, d;
    cin >> s >> t >> d;
    s--;
    t--;
    g[s][t] = d;
  }
  for (int i = 0; i < n; i++) g[i][i] = 0;

  long tot = 0;
  g = floyd_warshall(g, [&](long x, long y, long z) {
    long res = min(x, y + z);
    if (res != inf) tot += res;
    return res;
  });
  cout << tot << endl;
}
