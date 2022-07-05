#include <bits/stdc++.h>
using namespace std;

template<typename G, typename F> auto bfs(const G& g, F f, int src) -> void {
  queue<int> que;
  que.push(src);
  while(que.size()) {
    int u = que.front();
    que.pop();
    for(auto& v: g[u])
      if(f(u, v)) que.push(v);
  }
}

template<typename T, typename G>
auto bfs_sssp(const T& inf, const G& g, int src) -> vector<T> {
  int n = g.size();
  vector<T> dist(n, inf);
  dist[src] = 0;
  auto f = [&](int u, int v) -> bool {
    if(dist[v] != inf) return false;
    dist[v] = dist[u] + 1;
    return true;
  };
  bfs(g, f, src);
  return dist;
}

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, m;
  cin >> n >> m;

  int const inf = 1 << 30;
  int k = 3 * n;

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

  auto dist = bfs_sssp(inf, g, s);

  cout << (dist[t] == inf ? -1 : dist[t] / 3) << endl;
}
