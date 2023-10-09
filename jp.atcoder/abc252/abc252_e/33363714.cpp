#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  using tup = tuple<int, int, int>;
  vector<vector<tup>> g(n);
  for(int i = 0; i < m; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    a--;
    b--;
    g[a].emplace_back(b, c, i);
    g[b].emplace_back(a, c, i);
  }
  long const inf = 1l << 60;
  vector<long> dist(n, inf);
  dist[0] = 0;
  using pi = tuple<long, int>;
  priority_queue<pi, vector<pi>, greater<>> que;
  que.emplace(0, 0);
  vector<int> to_edge(n);
  while(que.size()) {
    auto [du, u] = que.top();
    que.pop();
    if(du > dist[u]) continue;
    for(auto& [v, w, eid]: g[u]) {
      long dv = du + w;
      if(dv >= dist[v]) continue;
      dist[v] = dv;
      to_edge[v] = eid;
      que.emplace(dv, v);
    }
  }
  for(int i = 1; i < n; i++) { cout << to_edge[i] + 1 << " \n"[i == n - 1]; }
}
