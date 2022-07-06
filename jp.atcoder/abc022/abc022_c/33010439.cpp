#include <bits/stdc++.h>
using namespace std;

template<typename G, typename F> auto floyd_warshall(G g, F f) -> G {
  int n = g.size();
  for(int k = 0; k < n; ++k) {
    for(int i = 0; i < n; ++i) {
      for(int j = 0; j < n; ++j) { g[i][j] = f(g[i][j], g[i][k], g[k][j]); }
    }
  }
  return g;
}

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, m;
  cin >> n >> m;

  int const inf = 1 << 29;

  vector<vector<int>> g(n, vector<int>(n, inf));
  vector<int> dist(n, inf);
  for(int i = 0; i < m; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    a--;
    b--;
    if(a == 0) {
      dist[b] = c;
    } else {
      g[a][b] = c;
      g[b][a] = c;
    }
  }

  for(int i = 0; i < n; i++) g[i][i] = 0;

  g = floyd_warshall(g, [](int x, int y, int z) { return min(x, y + z); });

  int mn = inf;
  for(int i = 1; i < n; i++) {
    for(int j = 1; j < i; j++) { mn = min(mn, dist[i] + dist[j] + g[i][j]); }
  }
  cout << (mn == inf ? -1 : mn) << endl;
}