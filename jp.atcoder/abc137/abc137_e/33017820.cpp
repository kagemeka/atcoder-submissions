#include <bits/stdc++.h>
using namespace std;

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

  vector<long> dist(n, inf);
  dist[0] = 0;
  for(int i = 0; i < 2 * (n - 1); i++) {
    for(auto& [u, v, w]: edges) {
      if(dist[u] == inf) continue;
      long dv = dist[u] + w;
      if(dv >= dist[v]) continue;
      dist[v] = i >= n - 1 ? -inf : dv;
    }
  }
  assert(dist[n - 1] != inf);
  // for(int i = 0; i < n; i++) { cout << dist[i] << " \n"[i == n - 1]; }
  cout << (dist[n - 1] == -inf ? -1 : max(0l, -dist[n - 1])) << endl;
}