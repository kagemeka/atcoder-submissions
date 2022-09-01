#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  vector<int> h(n);
  for(int i = 0; i < n; i++) cin >> h[i];
  vector<vector<pair<int, int>>> g(n);
  while(m--) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].emplace_back(v, max(0, h[v] - h[u]));
    g[v].emplace_back(u, max(0, h[u] - h[v]));
  }
  using pi = pair<long, int>;
  priority_queue<pi, vector<pi>, greater<>> que;
  que.emplace(0, 0);
  long const inf = 1l << 60;
  vector<long> dist(n, inf);
  dist[0] = 0;
  while(que.size()) {
    auto [du, u] = que.top();
    que.pop();
    if(du > dist[u]) continue;
    for(auto& [v, w]: g[u]) {
      long dv = du + w;
      if(dv >= dist[v]) continue;
      que.emplace(dv, v);
      dist[v] = dv;
    }
  }
  long mx = 0;
  for(int i = 0; i < n; i++) { mx = max(mx, h[0] - h[i] - dist[i]); }
  cout << mx << '\n';
}
