#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  vector<vector<int>> g(n);
  for(int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    g[u].push_back(v);
  }
  vector<int> preorder, low, order(n, n), labels(n, n);
  int ord = 0, label = 0;
  auto dfs = [&](auto&& f, int u) -> void {
    order[u] = ord;
    ord++;
    preorder.push_back(u);
    low.push_back(u);
    for(auto& v: g[u]) {
      if(order[v] == n) f(f, v);
      else if(labels[v] == n) {
        while(order[low.back()] > order[v]) low.pop_back();
      }
    }
    if(order[low.back()] < order[u]) return;
    while(true) {
      int v = preorder.back();
      preorder.pop_back();
      labels[v] = label;
      if(v == u) break;
    }
    label++;
    low.pop_back();
  };
  for(int i = 0; i < n; i++)
    if(labels[i] == n) dfs(dfs, i);
  int k = *max_element(labels.begin(), labels.end()) + 1;
  vector<vector<int>> comp(k);
  for(int i = 0; i < n; i++) comp[k - 1 - labels[i]].push_back(i);
  cout << k << endl;
  for(auto& comp: comp) {
    int n = comp.size();
    cout << n << ' ';
    for(int i = 0; i < n; i++) { cout << comp[i] << " \n"[i == n - 1]; }
  }
}
