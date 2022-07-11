#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
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
  function<void(int)> dfs;
  vector<bool> to_cycle(n);
  vector<int> state(n, false);
  int cnt = 0;
  dfs = [&](int u) {
    state[u] = 1;
    for(auto& v: g[u]) {
      if(state[v] == 0) {
        dfs(v);
      } else if(state[v] == 1) {
        to_cycle[u] = true;
      }
      to_cycle[u] = to_cycle[u] | to_cycle[v];
    }
    cnt += to_cycle[u];
    state[u] = 2;
  };
  for(int i = 0; i < n; i++) {
    if(state[i] >= 1) continue;
    dfs(i);
  }
  cout << cnt << endl;
}
