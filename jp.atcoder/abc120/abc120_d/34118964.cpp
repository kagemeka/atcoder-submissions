#include <bits/stdc++.h>
using namespace std;
struct union_find {
  vector<int> node;
  union_find(int size): node(size, -1) {}
  auto root(int u) -> int { return node[u] < 0 ? u : node[u] = root(node[u]); }
  auto unite(int u, int v) {
    u = root(u), v = root(v);
    if(u == v) return;
    if(node[u] > node[v]) swap(u, v);
    node[u] += node[v];
    node[v] = u;
  }
  auto size_of(int u) -> int { return -node[root(u)]; }
};
auto main() -> int {
  int n, m;
  cin >> n >> m;
  using pi = pair<int, int>;
  vector<pi> edges(m);
  for(int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    edges[i] = {u, v};
  }
  vector<long> res(m);
  long s = (long)n * (n - 1) >> 1;
  union_find uf(n);
  for(int i = m - 1; i >= 0; i--) {
    res[i] = s;
    auto& [u, v] = edges[i];
    if(uf.root(u) == uf.root(v)) continue;
    s -= (long)uf.size_of(u) * uf.size_of(v);
    uf.unite(u, v);
  }
  for(auto& x: res) cout << x << '\n';
}
