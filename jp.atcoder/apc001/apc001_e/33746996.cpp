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
    int need_c = 0;
    bool need_p = false;
    for(auto& v: g[u]) {
      if(v == p) continue;
      child++;
      auto [x, need_u] = dfs(v, u);
      need_c += need_u;
      s += x;
      c += x > 0;
    }
    // if (c == child && child > 1) need_p = false;
    // if(c >= 2) { need_p = false; }
    int d = max(0, (int)child - 1 - c);
    // if(d + c >= 2) need_p = false;
    s += d;
    if(p != -1 && (c != child || child == 0)) { need_p = true; }
    if(p == -1 && child <= 2 && c != 2 &&  need_c == child) { need_p = true; }
    if(p == -1 && need_p) s++;
    // cout << u << ' ' << s << endl;
    return {s, need_p};
  };
  cout << dfs(0, -1).first << endl;
}
