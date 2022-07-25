#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int const k = 1 << 13;
  int n, m, s;
  cin >> n >> m >> s;
  s = min(s, k);
  using tup = tuple<int, int, int>;
  vector<vector<tup>> g(n);
  for(int i = 0; i < m; i++) {
    int u, v, a, b;
    cin >> u >> v >> a >> b;
    u--;
    v--;
    g[u].emplace_back(v, a, b);
    g[v].emplace_back(u, a, b);
  }
  vector<int> c(n), d(n);
  for(int i = 0; i < n; i++) {
    cin >> c[i];
    c[i] = min(c[i], k);
    cin >> d[i];
  }
  long const inf = 1l << 60;
  vector<vector<long>> dp(n, vector<long>(k + 1, inf));
  dp[0][s] = 0;
  priority_queue<tuple<long, int, int>> que;
  que.emplace(0, 0, s);
  while(que.size()) {
    auto [du, u, cu] = que.top();
    que.pop();
    du *= -1;
    if(du > dp[u][cu]) continue;
    for(auto& [v, a, b]: g[u]) {
      int cv = cu - a;
      if(cv < 0) continue;
      long dv = du + b;
      if(dv >= dp[v][cv]) continue;
      dp[v][cv] = dv;
      que.emplace(-dv, v, cv);
    }
    int cv = min(k, cu + c[u]);
    long dv = du + d[u];
    if(dv >= dp[u][cv]) continue;
    dp[u][cv] = dv;
    que.emplace(-dv, u, cv);
  }
  for(int i = 1; i < n; i++) {
    cout << *min_element(dp[i].begin(), dp[i].end()) << endl;
  }
}
