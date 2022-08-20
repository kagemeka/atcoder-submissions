#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<vector<int>> g(n), t(n);
  for(int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    g[u].push_back(v);
    t[v].push_back(u);
  }
  vector<int> labels(n);
  vector<int> post_order;
  auto dfs = [&](auto&& f, int u) -> void {
    labels[u] = n;
    for(auto& v: g[u]) {
      if(labels[v] == n) continue;
      f(f, v);
    }
    post_order.push_back(u);
  };
  int label = 0;
  auto rdfs = [&](auto&& f, int u) -> void {
    labels[u] = label;
    for(auto& v: t[u]) {
      if(labels[v] != n) continue;
      f(f, v);
    }
  };
  for(int i = 0; i < n; i++) {
    if(labels[i] == 0) dfs(dfs, i);
  }
  for(int i = 0; i < n; i++) {
    int u = post_order[n - 1 - i];
    if(labels[u] != n) continue;
    rdfs(rdfs, u);
    label++;
  }
  int k = *max_element(labels.begin(), labels.end()) + 1;
  vector<vector<int>> comp(k);
  for(int i = 0; i < n; i++) comp[labels[i]].push_back(i);
  cout << k << endl;
  for(auto& comp: comp) {
    int n = comp.size();
    cout << n << ' ';
    for(int i = 0; i < n; i++) { cout << comp[i] << " \n"[i == n - 1]; }
  }
}
