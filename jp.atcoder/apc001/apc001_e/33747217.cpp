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
    int deg = 0, s = 0;
    vector<int> cnt;
    vector<bool> ok;
    for(auto& v: g[u]) {
      if(v == p) continue;
      auto [c, o] = dfs(v, u);
      deg += c >= 1;
      if(deg < (int)cnt.size()) {
        c = 1;
        o = true;
        deg++;
      }
      ok.push_back(o);
      cnt.push_back(c);
      s += c;
    }
    if(p == -1) {
      for(int i = 0; i < (int)cnt.size(); i++) {
        if(ok[i]) continue;
        if(deg - (cnt[i] >= 1) >= 1) continue;
        s += 1;
        break;
      }
    }
    return {s, deg == (int)cnt.size() && deg >= 1};
  };
  cout << dfs(0, -1).first << endl;
}
