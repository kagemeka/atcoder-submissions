#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  // h1 - d + hu
  int n, m;
  cin >> n >> m;
  vector<int> h(n);
  for(int i = 0; i < n; i++) cin >> h[i];
  using pi = pair<int, int>;
  vector<vector<pi>> g(n);
  for(int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    int d = h[v] - h[u];
    g[u].emplace_back(v, max(d, 0));
    g[v].emplace_back(u, max(-d, 0));
  }
  priority_queue<pair<long, int>> que;
  long const inf = 1l << 60;
  vector<long> dist(n, inf);
  dist[0] = 0;
  que.emplace(0, 0);
  while(que.size()) {
    auto [du, u] = que.top();
    que.pop();
    du *= -1;
    if(du > dist[u]) continue;
    for(auto& [v, w]: g[u]) {
      long dv = du + w;
      if(dv >= dist[v]) continue;
      dist[v] = dv;
      que.emplace(-dv, v);
    }
  }
  long mx = 0;
  for(int i = 0; i < n; i++) { mx = max(mx, h[0] - dist[i] - h[i]); }
  cout << mx << endl;
}
