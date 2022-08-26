#include <bits/stdc++.h>
using namespace std;
struct union_find {
  vector<int> data;
  union_find(int size): data(size, -1) {}
  auto size() -> int { return data.size(); }
  auto root(int u) -> int { return data[u] < 0 ? u : data[u] = root(data[u]); }
  auto unite(int u, int v) {
    u = root(u), v = root(v);
    if(u == v) return;
    if(data[u] > data[v]) swap(u, v);
    data[u] += data[v];
    data[v] = u;
  }
};
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m, q;
  cin >> n >> m >> q;
  using tup = tuple<int, int, int, int>;
  vector<tup> edges;
  int const inf = 1 << 30;
  for(int i = 0; i < m; i++) {
    int u, v, c;
    cin >> u >> v >> c;
    u--;
    v--;
    edges.emplace_back(c, inf, u, v);
  }
  for(int i = 0; i < q; i++) {
    int u, v, w;
    cin >> u >> v >> w;
    u--;
    v--;
    edges.emplace_back(w, i, u, v);
  }
  sort(edges.begin(), edges.end());
  vector<bool> res(q);
  union_find uf(n);
  for(auto& [w, i, u, v]: edges) {
    if(uf.root(u) == uf.root(v)) continue;
    if(i == inf) uf.unite(u, v);
    else res[i] = true;
  }
  for(auto x: res) cout << (x ? "Yes" : "No") << '\n';
}
