#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<vector<int>> g(n);
  for(int i = 0; i < n - 1; i++) {
    int u, v;
    cin >> u >> v;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  function<pair<int, bool>(int, int)> dfs;
  dfs = [&](int u, int p) -> pair<int, bool> {
    int s = 0;
    int c = 0;
    int child = 0;
    bool need_p = true;
    for(auto& v: g[u]) {
      if(v == p) continue;
      child++;
      auto [x, need_u] = dfs(v, u);
      // if(x > 0 && !need_u) { need_p = false; }
      s += x;
      c += x > 0;
    }
    if (c == child && child > 1) need_p = false;
    // if(c >= 2) { need_p = false; }
    int d = max(0, (int)child - 1 - c);
    // if(d + c >= 2) need_p = false;
    s += d;
    if(p == -1 && need_p && child == 1) s++;
    // cout << u << ' ' << s << endl;
    return {s, need_p};
  };
  cout << dfs(0, -1).first << endl;
}
