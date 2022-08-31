#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<vector<int>> g(n);
  while(m--) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].push_back(v);
  }
  vector<bool> ng(n);
  vector<int> visited(n);
  vector<int> on_stack(n);
  vector<int> depth(n, -1);
  vector<int> res;
  function<int(int)> dfs;
  dfs = [&](int u) -> int {
    if(on_stack[u]) { return u; }
    if(res.size()) return -1;
    on_stack[u] = true;
    visited[u] = true;
    int ret = -1;
    auto snap = ng;
    vector<int> cand1, cand2;
    for(auto& v: g[u]) {
      if(ng[v]) continue;
      if(on_stack[v]) cand1.push_back(v);
      else cand2.push_back(v);
      ng[v] = true;
    }
    sort(cand1.begin(), cand1.end(), [&](int i, int j) {
      return depth[i] > depth[j];
    });
    for(auto& v: (cand1.size() ? cand1 : cand2)) {
      if(snap[v]) continue;
      if(visited[v] && !on_stack[v]) continue;
      ng[v] = false;
      depth[v] = depth[u] + 1;
      int k = dfs(v);
      depth[v] = -1;
      ng[v] = true;
      if(k == -1 && !res.size()) continue;
      ret = k;
      break;
    }
    ng = snap;
    if(ret != -1) { res.push_back(u); }
    if(ret == u) { ret = -1; }
    on_stack[u] = false;
    return ret;
  };
  for(int i = 0; i < n; i++) {
    if(!visited[i]) {
      depth[i] = 0;
      dfs(i);
      depth[i] = -1;
    }
  }
  n = res.size();
  if(n) {
    cout << n << '\n';
    for(auto& x: res) cout << x + 1 << '\n';
  } else {
    cout << -1 << '\n';
  }
}
