#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<vector<int>> g(n);
  for(int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].push_back(v);
  }
  int s, t;
  cin >> s >> t;
  s--;
  t--;
  long const inf = 1l << 60;
  vector<vector<long>> dist(n, vector<long>(3, inf));
  dist[s][0] = 0;
  queue<pair<int, int>> que;
  que.emplace(s, 0);
  while(que.size()) {
    auto [u, r] = que.front();
    que.pop();
    for(auto& v: g[u]) {
      long dv = dist[u][r] + 1;
      int rv = (r + 1) % 3;
      if(dv >= dist[v][rv]) continue;
      dist[v][rv] = dv;
      que.emplace(v, rv);
    }
  }
  long res = dist[t][0];
  cout << (res == inf ? -1 : res / 3) << endl;
}
