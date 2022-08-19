#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> deg(n);
  for(int i = 0; i < n; i++) cin >> deg[i];
  using pi = pair<int, int>;
  vector<vector<pi>> g(n);
  for(int i = 0; i < n - 1; i++) {
    int u, v, w;
    cin >> u >> v >> w;
    u--;
    v--;
    g[u].emplace_back(v, w);
    g[v].emplace_back(u, w);
  }
  long s = 0;
  auto dfs = [&](auto&& dfs, int u, int p) -> vector<int> {
    vector<int> cand;
    for(auto [v, w]: g[u]) {
      if(v == p) continue;
      auto wv = dfs(dfs, v, u);
      if(deg[v] == 0 && wv.size()) { w -= wv.back(); }
      if(w <= 0 || (!deg[v] && !wv.size())) continue;
      cand.push_back(w);
    }
    sort(cand.rbegin(), cand.rend());
    while((int)cand.size() > deg[u]) { cand.pop_back(); }
    deg[u] -= cand.size();
    for(auto& x: cand) { s += x; }
    return cand;
  };
  dfs(dfs, 0, -1);
  cout << s << endl;
}
