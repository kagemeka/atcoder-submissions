#include <bits/stdc++.h>
using namespace std;
struct union_find {
  vector<int> data;
  union_find(int size): data(size, -1) {}
  auto root(int u) -> int { return data[u] < 0 ? u : data[u] = root(data[u]); }
  auto unite(int u, int v) {
    u = root(u), v = root(v);
    if(u == v) return;
    if(data[u] > data[v]) swap(u, v);
    data[u] += data[v];
    data[v] = u;
  }
  auto size_of(int u) -> int { return -data[root(u)]; }
};
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m, e;
  cin >> n >> m >> e;
  vector<pair<int, int>> edges;
  for(int i = 0; i < e; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    if(u >= n) u = n;
    if(v >= n) v = n;
    edges.emplace_back(u, v);
  }
  vector<bool> will_remain(e, true);
  int q;
  cin >> q;
  vector<int> queries(q);
  for(int i = 0; i < q; i++) {
    cin >> queries[i];
    queries[i]--;
    will_remain[queries[i]] = false;
  }
  union_find uf(n + 1);
  for(int i = 0; i < e; i++) {
    if(!will_remain[i]) continue;
    auto& [u, v] = edges[i];
    uf.unite(u, v);
  }
  vector<int> res(q);
  for(int i = q; i-- > 0;) {
    res[i] = uf.size_of(n) - 1;
    auto& [u, v] = edges[queries[i]];
    uf.unite(u, v);
  }
  for(auto& x: res) cout << x << '\n';
}
