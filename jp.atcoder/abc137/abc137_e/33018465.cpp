#include <bits/stdc++.h>
using namespace std;

template<typename G, typename F> auto bellman_ford(const G& edges, F f)
  -> void {
  while(true) {
    bool updated = false;
    for(auto& e: edges) { updated |= f(e); }
    if(!updated) break;
  }
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
  vector<long> dist(n, inf);
  dist[0] = 0;

  long iter_cnt = 0;
  m = edges.size();
  auto f = [&](tup const& e) -> bool {
    iter_cnt++;
    int loop = (iter_cnt + m - 1) / m;
    auto& [u, v, w] = e;
    if(dist[u] == inf) return false;
    auto dv = dist[u] == -inf ? -inf : dist[u] + w;
    if(dv >= dist[v]) return false;
    dist[v] = loop >= n - 1 ? -inf : dv;
    return true;
  };

  bellman_ford(edges, f);
  cout << (dist[n - 1] == -inf ? -1 : max(0l, -dist[n - 1])) << endl;
}