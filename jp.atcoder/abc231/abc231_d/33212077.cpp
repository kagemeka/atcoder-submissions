#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  // 1. deg <= 2 (at most n - 2), deg <= 1 (at most 2)
  // 2. no cycle
  // deg <= 2 and satisfy 2 -> satisfy 1
  int n, m;
  cin >> n >> m;
  vector<vector<int>> g(n);
  vector<int> deg(n);
  for(int i = 0; i < m; i++) {
    int a, b;
    cin >> a >> b;
    a--;
    b--;
    g[a].push_back(b);
    g[b].push_back(a);
    deg[a]++;
    deg[b]++;
  }
  for(auto& d: deg) {
    if(d >= 3) {
      cout << "No" << endl;
      return 0;
    }
  }
  vector<bool> visited(n);
  function<bool(int, int)> dfs;
  dfs = [&](int u, int p) -> bool {
    visited[u] = true;
    for(auto& v: g[u]) {
      if(v == p) continue;
      if(visited[v]) return false;
      dfs(v, u);
    }
    return true;
  };
  bool ok = true;
  for(int i = 0; i < n; i++) {
    if(visited[i]) continue;
    ok &= dfs(i, -1);
  }
  cout << (ok ? "Yes" : "No") << endl;
}
