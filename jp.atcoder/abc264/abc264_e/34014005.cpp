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
  auto size() -> int { return data.size(); }
  auto labels() -> vector<int> {
    int n = size();
    vector<int> labels(n, -1);
    int l = 0;
    for(int i = 0; i < n; i++) {
      int r = root(i);
      if(labels[r] == -1) {
        labels[r] = l;
        l++;
      }
      labels[i] = labels[r];
    }
    return labels;
  }
};
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m, e;
  cin >> n >> m >> e;
  using pi = pair<int, int>;
  vector<pi> edges;
  for(int i = 0; i < e; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    edges.emplace_back(u, v);
  }
  int q;
  cin >> q;
  vector<int> queries(q);
  for(int i = 0; i < q; i++) {
    cin >> queries[i];
    queries[i]--;
  }
  reverse(queries.begin(), queries.end());
  vector<bool> connected(n);
  int cnt = 0;
  union_find uf(n);
  vector<int> res;
  vector<bool> will_remain(e, true);
  for(int i: queries) { will_remain[i] = false; }
  for(int i = 0; i < e; i++) {
    if(!will_remain[i]) continue;
    auto [u, v] = edges[i];
    // cout << u << ' ' << v << endl;
    if(u >= n && v >= n) { continue; }
    if(v >= n) {
      int r = uf.root(u);
      if(!connected[r]) { cnt += uf.size_of(r); }
      connected[r] = true;
    } else {
      int ru = uf.root(u);
      int rv = uf.root(v);
      if(connected[ru] && !connected[rv]) {
        connected[rv] = true;
        cnt += uf.size_of(rv);
      } else if(!connected[ru] && connected[rv]) {
        connected[ru] = true;
        cnt += uf.size_of(ru);
      }
      uf.unite(ru, rv);
    }
  }
  for(int i: queries) {
    res.push_back(cnt);
    auto [u, v] = edges[i];
    if(u >= n && v >= n) { continue; }
    if(v >= n) {
      int r = uf.root(u);
      if(!connected[r]) { cnt += uf.size_of(r); }
      connected[r] = true;
      // cnt += 1;
      // cout << -1 << endl;
    } else {
      // cout << -1 << endl;
      int ru = uf.root(u);
      int rv = uf.root(v);
      if(connected[ru] && !connected[rv]) {
        connected[rv] = true;
        cnt += uf.size_of(rv);
      } else if(!connected[ru] && connected[rv]) {
        connected[ru] = true;
        cnt += uf.size_of(ru);
      }
      uf.unite(ru, rv);
    }
  }
  reverse(res.begin(), res.end());
  for(auto& x: res) { cout << x << endl; }
}
