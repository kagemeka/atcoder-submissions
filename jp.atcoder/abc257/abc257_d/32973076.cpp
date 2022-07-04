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

  int n;
  cin >> n;

  long inf = 1l << 60;
  vector<vector<long>> g(n, vector<long>(n, inf));
  for (int i = 0; i < n; i++) g[i][i] = 0;

  vector<tuple<long, long, long>> a(n);
  for (int i = 0; i < n; i++) {
    long x, y, p;
    cin >> x >> y >> p;
    a[i] = {x, y, p};
  }
  for (int i = 0; i < n; i++) {
    auto [xi, yi, pi] = a[i];
    for (int j = 0; j < n; j++) {
      auto [xj, yj, _] = a[j];
      g[i][j] = (abs(xj - xi) + abs(yj - yi) + pi - 1) / pi;
    }
  }

  auto f = [](long x, long y, long z) { return min(x, max(y, z)); };
  g = floyd_warshall(g, f);

  long mn = inf;
  for (auto& row : g) {
    mn = min(mn, *max_element(row.begin(), row.end()));
  }
  cout << mn << endl;
}
