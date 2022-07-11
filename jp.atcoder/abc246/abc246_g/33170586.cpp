#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n - 1; i++) cin >> a[i + 1];
  vector<vector<int>> g(n);
  for(int i = 0; i < n - 1; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  auto possible = [&](int k) -> bool {
    function<int(int, int)> dfs;
    dfs = [&](int u, int p) -> int {
      int to_guard = 0;
      for(auto& v: g[u]) {
        if(v == p) continue;
        to_guard += max(0, dfs(v, u) - 1);
        to_guard += a[v] >= k;
      }
      return to_guard;
    };
    return dfs(0, 0) >= 2;
  };
  int ok = 0, ng = 1 << 30;
  while(ng - ok > 1) {
    int k = (ng + ok) >> 1;
    if(possible(k)) ok = k;
    else ng = k;
  }
  cout << ok << endl;
}
