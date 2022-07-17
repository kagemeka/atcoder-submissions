#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int s, t, m;
  cin >> s >> t >> m;
  using pi = pair<int, int>;
  vector<pi> edges;
  int n = s + t;
  vector<vector<int>> g(n);
  for(int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].push_back(v);
    g[v].push_back(u);
    edges.emplace_back(u, v);
  }
  vector<int> parent(n, -1);
  vector<int> depth(n, -1);
  depth[0] = 0;
  function<void(int)> dfs;
  dfs = [&](int u) {
    for(int v: g[u]) {
      if(depth[v] != -1) continue;
      parent[v] = u;
      depth[v] = depth[u] + 1;
      dfs(v);
    }
  };
  // queue<int> que;
  // que.push(0);
  // while(que.size()) {
  //   int u = que.front();
  //   que.pop();
  //   for(int v: g[u]) {
  //     if(v == parent[u]) continue;
  //     parent[v] = u;
  //     depth[v] = depth[u] + 1;
  //     que.push(v);
  //   }
  // }
  dfs(0);
  for(auto& [u, v]: edges) {
    if(depth[u] > depth[v]) swap(u, v);
    if(depth[u] + 3 != depth[v]) continue;
    vector<int> res;
    while(v != u) {
      res.push_back(v);
      v = parent[v];
    }
    res.push_back(u);
    for(int i = 0; i < 4; i++) { cout << res[i] + 1 << " \n"[i == 3]; }
    return 0;
  }
  cout << -1 << endl;
}
