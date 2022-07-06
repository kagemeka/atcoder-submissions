#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, m;
  cin >> n >> m;

  using p = pair<int, int>;

  vector<vector<p>> g(n);
  while(m--) {
    int u, v, c;
    cin >> u >> v >> c;
    u--;
    v--;
    g[u].emplace_back(v, c);
    g[v].emplace_back(u, c);
  }

  vector<int> res(n, -1);
  res[0] = 1;

  function<void(int)> dfs;
  dfs = [&](int u) {
    for(auto& [v, c]: g[u]) {
      if(res[v] != -1) continue;
      res[v] = res[u] != c ? c : 1 + (c == 1);
      dfs(v);
    }
  };
  dfs(0);
  for(auto& c: res) { cout << c << endl; }
}