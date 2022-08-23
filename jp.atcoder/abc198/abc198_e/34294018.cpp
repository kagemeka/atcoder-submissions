#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> c(n);
  for(int i = 0; i < n; i++) cin >> c[i];
  vector<vector<int>> g(n);
  for(int i = 0; i < n - 1; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  vector<int> cnt(1 << 17);
  vector<int> res;
  auto dfs = [&](auto&& dfs, int u, int p) -> void {
    int x = c[u];
    if(cnt[x]++ == 0) res.push_back(u);
    for(auto& v: g[u]) {
      if(v == p) continue;
      dfs(dfs, v, u);
    }
    cnt[x]--;
  };
  dfs(dfs, 0, -1);
  sort(res.begin(), res.end());
  for(auto& x: res) cout << x + 1 << '\n';
}
