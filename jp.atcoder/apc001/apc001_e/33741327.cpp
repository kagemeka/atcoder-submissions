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
  function<int(int, int)> dfs;
  dfs = [&](int u, int p) -> int {
    int s = 0;
    int c = 0;
    int child = 0;
    for(auto& v: g[u]) {
      if(v == p) continue;
      child++;
      int x = dfs(v, u);
      s += x;
      c += x > 0;
    }
    s += max(0, (int)child - 1 - c);
    if(p == -1 && child == 1) s++;
    return s;
  };
  cout << dfs(0, -1) << endl;
}
