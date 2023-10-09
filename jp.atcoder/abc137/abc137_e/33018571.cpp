#include <bits/stdc++.h>
using namespace std;

template<typename G, typename F> auto bellman_ford_abstract(const G& edges, F f)
  -> void {
  while(true) {
    bool updated = false;
    for(auto& e: edges) { updated |= f(e); }
    if(!updated) break;
  }
}

template<typename G, typename T>
auto bellman_ford_sssp(const T& inf, int n, const G& edges, int src)
  -> vector<T> {
  vector<T> dist(n, inf);
  dist[src] = 0;
  long iter_cnt = 0;
  int m = edges.size();
  auto f = [&](tuple<int, int, T> const& e) -> bool {
    iter_cnt++;
    int loop = (iter_cnt + m - 1) / m;
    auto& [u, v, w] = e;
    if(dist[u] == inf) return false;
    auto dv = dist[u] == -inf ? -inf : dist[u] + w;
    if(dv >= dist[v]) return false;
    dist[v] = loop >= n ? -inf : dv;
    return true;
  };
  bellman_ford_abstract(edges, f);
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
    edges.emplace_back(--a, --b, p - c);
  }

  long const inf = 1l << 60;
  auto dist = bellman_ford_sssp(inf, n, edges, 0);
  cout << (dist[n - 1] == -inf ? -1 : max(0l, -dist[n - 1])) << endl;
}
