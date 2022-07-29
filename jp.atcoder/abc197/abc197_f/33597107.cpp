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
  for(int i = 0; i < m; i++) {
    int u, v;
    char c;
    cin >> u >> v >> c;
    u--;
    v--;
    int x = c - 'a';
    g[u].emplace_back(v, x);
    g[v].emplace_back(u, x);
  }
  dp[0][n - 1] = 0;
  que.emplace(0, n - 1);
  while(que.size()) {
    auto [u, v] = que.front();
    que.pop();
    for(auto [nu, x]: g[u]) {
      for(auto [nv, y]: g[v]) {
        if(x != y) continue;
        int d = dp[u][v] + 1;
        if(d >= dp[nu][nv]) continue;
        dp[nu][nv] = d;
        que.emplace(nu, nv);
      }
    }
  }
  int d = dp[n - 1][0];
  cout << (d == inf ? -1 : d) << endl;
}
