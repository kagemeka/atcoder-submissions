#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  vector<vector<int>> g(n);
  for(int i = 0; i < n - 1; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  int const inf = 1 << 30;
  vector<int> lis(n, inf);
  vector<int> res(n);
  function<void(int, int)> dfs;
  dfs = [&](int u, int p) {
    auto it = lower_bound(lis.begin(), lis.end(), a[u]);
    int prev = *it;
    *it = a[u];
    res[u] = lower_bound(lis.begin(), lis.end(), inf) - lis.begin();
    for(auto& v: g[u]) {
      if(v == p) continue;
      dfs(v, u);
    }
    *it = prev;
  };
  dfs(0, -1);
  for(auto& x: res) cout << x << endl;
}
