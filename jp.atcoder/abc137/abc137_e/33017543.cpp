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

  int const inf = 1 << 29;

  vector<int> dist(n, inf);
  dist[0] = 0;
  for(int i = 0; i < n; i++) {
    for(auto& [u, v, w]: edges) {
      if(dist[u] == inf) continue;
      int dv = dist[u] + w;
      if(dv >= dist[v]) continue;
      dist[v] = i == n - 1 ? -inf : dv;
    }
  }
  cout << (dist[n - 1] == -inf ? -1 : max(0, -dist[n - 1])) << endl;
}
