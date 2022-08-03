#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, u0, v0;
  cin >> n >> u0 >> v0;
  u0--;
  v0--;
  vector<vector<int>> g(n);
  for(int i = 0; i < n - 1; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  int const inf = 1 << 1 << 29;
  vector<int> dist(n, 0);
  vector<int> parent(n, -1);
  function<void(int)> dfs;
  dfs = [&](int u) {
    for(auto& v: g[u]) {
      if(v == parent[u]) continue;
      parent[v] = u;
      dist[v] = max(dist[v], dist[u] + 1);
      dfs(v);
    }
  };
  dfs(v0);
  int d = dist[u0];
  int d0 = (d - 1) >> 1;
  for(int i = 0; i < d0; i++) { u0 = parent[u0]; }
  for(int i = 0; i < n; i++) dist[i] = -inf;
  dist[u0] = 0;
  dfs(v0);
  int res = d0 + *max_element(dist.begin(), dist.end()) + ((d & 1) ^ 1);
  cout << res << endl;
}
