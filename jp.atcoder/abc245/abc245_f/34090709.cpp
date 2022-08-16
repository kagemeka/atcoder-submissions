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
  function<void(int u)> dfs;
  vector<int> state(n);
  dfs = [&](int u) {
    state[u] = 1; // on stack
    for(auto& v: g[u]) {
      auto& s = state[v];
      if(s == 0) dfs(v);
      if(s == 1 || s == 3) { // on stack or to cycle
        state[u] = 3; // to cycle
      }
    }
    state[u] = max(state[u], 2);
  };
  dfs(0);
  int c = 0;
  for(auto& x: state) c += x == 3;
  cout << c << endl;
}
