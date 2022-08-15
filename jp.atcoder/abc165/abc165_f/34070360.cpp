#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int const inf = 1 << 30;
  vector<vector<int>> g(n);
  for(int i = 0; i < n - 1; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  vector<int> lis(n, inf);
  function<void(int, int)> dfs;
  vector<int> res(n);
  dfs = [&](int u, int p) {
    int x = a[u];
    auto it = lower_bound(lis.begin(), lis.end(), x);
    int pre = *it;
    *it = x;
    res[u] = lower_bound(lis.begin(), lis.end(), inf) - lis.begin();
    for(int v: g[u]) {
      if(v == p) continue;
      dfs(v, u);
    }
    *it = pre;
  };
  dfs(0, -1);
  for(int i = 0; i < n; i++) cout << res[i] << '\n';
}
