#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  vector<vector<int>> g(n + 1);
  for(int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  int const inf = 1 << 29;
  auto bfs = [&](int src) -> vector<int> {
    vector<int> dist(n + 1, inf);
    queue<int> que;
    dist[src] = 0;
    que.push(src);
    while(que.size()) {
      int u = que.front();
      que.pop();
      for(int v: g[u]) {
        int dv = dist[u] + 1;
        if(dv >= dist[v]) continue;
        dist[v] = dv;
        que.push(v);
      }
    }
    return dist;
  };
  auto d1 = bfs(1);
  auto dn = bfs(n);
  for(int i = 1; i <= n; i++) {
    auto res = d1[n];
    res = min(res, min(d1[0], d1[i]) + min(dn[0], dn[i]));
    cout << (res == inf ? -1 : res) << " \n"[i == n];
  }
}
