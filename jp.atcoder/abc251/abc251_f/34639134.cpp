#include <bits/stdc++.h>
using namespace std;
auto graph_from_edges(int n, vector<pair<int, int>> edges)
  -> vector<vector<pair<int, int>>> {
  vector<vector<pair<int, int>>> g(n);
  for(int i = 0; i < (int)edges.size(); i++) {
    auto& [u, v] = edges[i];
    g[u].emplace_back(v, i);
    g[v].emplace_back(u, i);
  }
  return g;
}
// return eid
auto bfs_tree(int n, vector<pair<int, int>> edges, int src) -> vector<bool> {
  int m = edges.size();
  vector<bool> used(m);
  auto g = graph_from_edges(n, edges);
  queue<int> que;
  que.push(src);
  vector<bool> to_que(n);
  to_que[src] = true;
  while(que.size()) {
    int u = que.front();
    que.pop();
    for(auto& [v, eid]: g[u]) {
      if(to_que[v]) continue;
      used[eid] = true;
      to_que[v] = true;
      que.push(v);
    }
  }
  return used;
}
auto dfs_tree(int n, vector<pair<int, int>> edges, int src) -> vector<bool> {
  int m = edges.size();
  vector<bool> used(m);
  auto g = graph_from_edges(n, edges);
  vector<bool> visited(n);
  auto dfs = [&](auto&& f, int u) -> void {
    visited[u] = true;
    for(auto& [v, eid]: g[u]) {
      if(visited[v]) continue;
      used[eid] = true;
      f(f, v);
    }
  };
  dfs(dfs, src);
  return used;
}
auto main() -> int {
  // dfs tree / bfs tree
  int n, m;
  cin >> n >> m;
  vector<pair<int, int>> edges(m);
  for(int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    edges[i] = {u, v};
  }
  auto dt = dfs_tree(n, edges, 0);
  auto bt = bfs_tree(n, edges, 0);
  for (int i = 0; i < m; i++) {
    if (!dt[i]) continue;
    auto&[u, v] = edges[i];
    cout << i + 1 << ' ' << v + 1 << '\n';
  }
  for(int i = 0; i < m; i++) {
    if(!bt[i]) continue;
    auto& [u, v] = edges[i];
    cout << i + 1 << ' ' << v + 1 << '\n';
  }
}
