#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  using p = pair<int, int>;
  vector<vector<p>> g(n);
  for(int i = 0; i < n - 1; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    a--;
    b--;
    g[a].emplace_back(b, c);
    g[b].emplace_back(a, c);
  }
  int q, k;
  cin >> q >> k;
  queue<int> que;
  k--;
  que.push(k);
  vector<long> dist(n);
  vector<int> parent(n, n);
  dist[k] = 0;
  while(que.size()) {
    auto u = que.front();
    que.pop();
    for(auto& [v, w]: g[u]) {
      if(v == parent[u]) continue;
      parent[v] = u;
      dist[v] = dist[u] + w;
      que.push(v);
    }
  }
  while(q--) {
    int x, y;
    cin >> x >> y;
    cout << dist[--x] + dist[--y] << endl;
  }
}
