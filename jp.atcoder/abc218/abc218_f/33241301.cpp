#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  // edges on shortest path is most N - 1 out of M
  // O((N + M)N;
  int n, m;
  cin >> n >> m;
  vector<vector<bool>> on_path(n, vector<bool>(n));
  vector<vector<int>> g(n);
  vector<pair<int, int>> edges(m);
  for(int i = 0; i < m; i++) {
    int s, t;
    cin >> s >> t;
    s--;
    t--;
    g[s].push_back(t);
    edges[i] = {s, t};
  }
  vector<int> dist(n);
  vector<int> pre(n);
  int const inf = 1 << 29;
  queue<int> que;
  auto bfs = [&](int src, int no_u = -1, int no_v = -1) {
    for(int i = 0; i < n; i++) {
      dist[i] = inf;
      pre[i] = -1;
    }
    dist[src] = 0;
    que.push(src);
    while(que.size()) {
      int u = que.front();
      que.pop();
      for(int& v: g[u]) {
        if(u == no_u && v == no_v) continue;
        int dv = dist[u] + 1;
        if(dv >= dist[v]) continue;
        dist[v] = dv;
        pre[v] = u;
        que.push(v);
      }
    }
  };
  bfs(0);
  int v = n - 1;
  while(pre[v] != -1) {
    on_path[pre[v]][v] = true;
    v = pre[v];
  }
  int d0 = dist[n - 1];
  for(auto& [u, v]: edges) {
    int d;
    if(!on_path[u][v]) {
      d = d0;
    } else {
      bfs(0, u, v);
      d = dist[n - 1];
    }
    cout << (d == inf ? -1 : d) << endl;
  }
}
