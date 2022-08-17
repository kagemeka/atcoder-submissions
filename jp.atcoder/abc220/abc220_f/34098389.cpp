#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<vector<int>> g(n);
  for(int i = 0; i < n - 1; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  function<void(int, int)> pull_dfs, push_dfs;
  vector<long> dist_sum(n);
  vector<long> size(n, 1);
  pull_dfs = [&](int u, int p) {
    for(auto& v: g[u]) {
      if(v == p) continue;
      pull_dfs(v, u);
      size[u] += size[v];
      dist_sum[u] += dist_sum[v] + size[v];
    }
  };
  push_dfs = [&](int u, int p) {
    for(auto& v: g[u]) {
      if(v == p) continue;
      dist_sum[v] += dist_sum[u] - dist_sum[v] - size[v] + n - size[v];
      push_dfs(v, u);
    }
  };
  pull_dfs(0, -1);
  push_dfs(0, -1);
  for(auto& x: dist_sum) { cout << x << '\n'; }
}
