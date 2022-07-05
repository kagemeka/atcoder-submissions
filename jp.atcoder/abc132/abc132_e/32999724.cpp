#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, m;
  cin >> n >> m;

  int const inf = 1 << 30;
  int k = 3 * n;
  vector<int> dist(k, inf);

  vector<vector<int>> g(k);

  while(m--) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    for(int i = 0; i < 3; i++) {
      g[u + i * n].push_back((v + (i + 1) * n) % k);
    }
  }

  int s, t;
  cin >> s >> t;
  s--;
  t--;
  dist[s] = 0;
  queue<int> que;
  que.push(s);

  while(que.size()) {
    int u = que.front();
    que.pop();
    for(auto& v: g[u]) {
      if(dist[v] != inf) continue;
      dist[v] = dist[u] + 1;
      que.push(v);
    }
  }

  cout << (dist[t] == inf ? -1 : dist[t] / 3) << endl;
}
