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

  vector<tuple<int, int, int>> edges;
  for (int i = 0; i < m; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    a--;
    b--;
    edges.emplace_back(a, b, c);
  }

  long inf = 1l << 60;
  vector<vector<long>> g(n, vector<long>(n, inf));
  for (auto& [a, b, c] : edges) {
    g[a][b] = c;
    g[b][a] = c;
  }
  for (int i = 0; i < n; i++) g[i][i] = 0;

  g = floyd_warshall(g, [](long x, long y, long z) { return min(x, y + z); });

  int cnt = 0;
  for (auto& [i, j, c] : edges) {
    for (int k = 0; k < n; k++) {
      if (g[i][k] + g[k][j] < c) {
        cnt++;
        break;
      }
    }
  }
  cout << cnt << endl;
}
