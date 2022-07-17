#include <bits/stdc++.h>
using namespace std;
struct union_find {
  vector<int> data;
  union_find(int size): data(size, -1) {}
  auto root(int u) -> int { return data[u] < 0 ? u : data[u] = root(data[u]); }
  auto unite(int u, int v) {
    u = root(u), v = root(v);
    if(u == v) return;
    if(data[u] > data[v]) swap(u, v);
    data[u] += data[v];
    data[v] = u;
  }
};
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> p(n);
  for(int i = 0; i < n; i++) {
    cin >> p[i];
    p[i]--;
  }
  int m;
  cin >> m;
  struct edge {
    int to, id;
    edge(int to, int id): to(to), id(id) {}
  };
  vector<vector<edge>> g(n);
  union_find uf(n);
  for(int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    if(uf.root(u) == uf.root(v)) continue;
    uf.unite(u, v);
    g[u].emplace_back(v, i);
    g[v].emplace_back(u, i);
  }
  for(int i = 0; i < n; i++) {
    if(uf.root(i) != uf.root(p[i])) {
      cout << -1 << endl;
      return 0;
    }
  }
  vector<int> res;
  function<void(int, int)> dfs;
  function<bool(int, int, int)> fetch;
  fetch = [&](int u, int par, int t) -> bool {
    if(p[u] == t) return true;
    for(auto& [v, eid]: g[u]) {
      if(v == par) continue;
      if(!fetch(v, u, t)) continue;
      swap(p[u], p[v]);
      res.push_back(eid);
      return true;
    }
    return false;
  };
  dfs = [&](int u, int p) {
    for(auto& [v, _]: g[u]) {
      if(v == p) continue;
      dfs(v, u);
    }
    fetch(u, -1, u);
  };
  for(int i = 0; i < n; i++) {
    if(i != uf.root(i)) continue;
    dfs(i, -1);
  }
  cout << res.size() << endl;
  for(int i = 0; i < (int)res.size(); i++) {
    cout << res[i] + 1 << " \n"[i == (int)res.size() - 1];
  }
}
