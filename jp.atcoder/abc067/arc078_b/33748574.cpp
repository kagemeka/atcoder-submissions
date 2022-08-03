#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
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
  function<void(int)> dfs;
  vector<int> depth(n, 0);
  vector<int> parent(n, -1);
  vector<int> size(n, 1);
  dfs = [&](int u) {
    for(auto& v: g[u]) {
      if(v == parent[u]) continue;
      parent[v] = u;
      depth[v] = depth[u] + 1;
      dfs(v);
      size[u] += size[v];
    }
  };
  dfs(0);
  int v = n - 1;
  int d = (depth[v] - 1) >> 1;
  for(int i = 0; i < d; i++) { v = parent[v]; }
  cout << (size[0] - size[v] > size[v] ? "Fennec" : "Snuke") << endl;
}
