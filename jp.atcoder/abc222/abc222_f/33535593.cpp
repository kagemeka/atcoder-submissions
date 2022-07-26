#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  using pi = pair<int, int>;
  vector<vector<pi>> g(n);
  for(int i = 0; i < n - 1; i++) {
    int u, v, w;
    cin >> u >> v >> w;
    u--;
    v--;
    g[u].emplace_back(v, w);
    g[v].emplace_back(u, w);
  }
  vector<int> d(n);
  for(int i = 0; i < n; i++) cin >> d[i];
  vector<long> dist(n);
  function<void(int, int)> calc_dist;
  calc_dist = [&](int u, int p) {
    for(auto& [v, w]: g[u]) {
      if(v == p) continue;
      dist[v] = dist[u] + w;
      calc_dist(v, u);
    }
  };
  auto init_dist = [&]() {
    for(int i = 0; i < n; i++) dist[i] = 0;
  };
  auto get_farthest = [&](int u) -> int {
    init_dist();
    calc_dist(u, -1);
    int v = -1;
    long mx = -1;
    for(int i = 0; i < n; i++) {
      if(i == u) continue;
      dist[i] += d[i];
      if(dist[i] > mx) {
        v = i;
        mx = dist[i];
      }
    }
    return v;
  };
  int s0 = get_farthest(0);
  int s1 = get_farthest(s0);
  auto calc_costs = [&](int u) -> vector<long> {
    init_dist();
    calc_dist(u, -1);
    for(int i = 0; i < n; i++) {
      if(i == u) continue;
      dist[i] += d[u];
    }
    return dist;
  };
  auto c0 = calc_costs(s0);
  auto c1 = calc_costs(s1);
  for(int i = 0; i < n; i++) { cout << max(c0[i], c1[i]) << endl; }
}
