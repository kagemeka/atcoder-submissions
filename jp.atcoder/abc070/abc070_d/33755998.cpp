#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<vector<pair<int, int>>> g(n);
  for(int i = 0; i < n - 1; i++) {
    int u, v, c;
    cin >> u >> v >> c;
    u--;
    v--;
    g[u].emplace_back(v, c);
    g[v].emplace_back(u, c);
  }
  int q, k;
  cin >> q >> k;
  k--;
  vector<long> dist(n);
  dist[k] = 0;
  queue<int> que;
  que.push(k);
  vector<int> parent(n, -1);
  while(que.size()) {
    int u = que.front();
    que.pop();
    for(auto& [v, w]: g[u]) {
      if(v == parent[u]) continue;
      parent[v] = u;
      dist[v] = dist[u] + w;
      que.push(v);
    }
  }
  for(int i = 0; i < q; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    cout << dist[u] + dist[v] << endl;
  }
}
