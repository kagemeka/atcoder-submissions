#include <bits/stdc++.h>
using namespace std;

template<typename T, typename G>
auto bellman_ford(const T& inf, int n, const G& edges, int src) -> vector<T> {
  vector<T> dist(n, inf);
  dist[src] = 0;
  for(int i = 0; i < 2 * (n - 1); i++) {
    for(auto& [u, v, w]: edges) {
      if(dist[u] == inf) continue;
      T dv = dist[u] == -inf ? -inf : dist[u] + w;
      if(dv >= dist[v]) continue;
      dist[v] = i >= n - 1 ? -inf : dv;
    }
  }
  return dist;
}

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, m, p;
  cin >> n >> m >> p;

  using tup = tuple<int, int, int>;
  vector<tup> edges;
  while(m--) {
    int a, b, c;
    cin >> a >> b >> c;
    edges.emplace_back(--a, --b, p - c); // reverse sign
  }

  long const inf = 1l << 60;
  auto dist = bellman_ford(inf, n, edges, 0);
  cout << (dist[n - 1] == -inf ? -1 : max(0l, -dist[n - 1])) << endl;
}
