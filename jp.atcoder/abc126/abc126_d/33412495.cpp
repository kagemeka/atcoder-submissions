#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  using p = pair<int, int>;
  vector<vector<p>> g(n);
  for(int i = 0; i < n - 1; i++) {
    int u, v, w;
    cin >> u >> v >> w;
    u--;
    v--;
    g[u].emplace_back(v, w);
    g[v].emplace_back(u, w);
  }
  queue<int> que;
  vector<long> dist(n, -1);
  dist[0] = 0;
  que.push(0);
  while(que.size()) {
    int u = que.front();
    que.pop();
    for(auto& [v, w]: g[u]) {
      if(dist[v] != -1) continue;
      dist[v] = dist[u] + w;
      que.push(v);
    }
  }
  for(int i = 0; i < n; i++) { cout << (dist[i] & 1) << endl; }
}
