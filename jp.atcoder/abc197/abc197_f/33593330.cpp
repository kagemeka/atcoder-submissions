#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  using pi = pair<int, int>;
  vector<vector<pi>> g(n);
  int const inf = 1 << 29;
  vector<vector<int>> dp(n, vector<int>(n, inf));
  queue<pi> que;
  for(int i = 0; i < n; i++) {
    dp[i][i] = 0;
    que.emplace(i, i);
  }
  for(int i = 0; i < m; i++) {
    int u, v;
    char c;
    cin >> u >> v >> c;
    u--;
    v--;
    int x = c - 'a';
    g[u].emplace_back(v, x);
    g[v].emplace_back(u, x);
    if(u > v) swap(u, v);
    dp[u][v] = min(dp[u][v], 1);
    que.emplace(u, v);
  }
  while(que.size()) {
    auto [u, v] = que.front();
    que.pop();
    for(auto [nu, x]: g[u]) {
      for(auto [nv, y]: g[v]) {
        if(x != y) continue;
        int d = dp[u][v] + 2;
        if(nu > nv) swap(nu, nv);
        if(d >= dp[nu][nv]) continue;
        dp[nu][nv] = d;
        que.emplace(nu, nv);
      }
    }
  }
  int d = dp[0][n - 1];
  cout << (d == inf ? -1 : d) << endl;
}
