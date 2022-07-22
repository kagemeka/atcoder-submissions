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
};
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  // vector<set<int>> g(n);
  union_find uf(n);
  while(m--) {
    int a, b;
    cin >> a >> b;
    uf.unite(--a, --b);
  }
  int mx = 0;
  for(int i = 0; i < n; i++) mx = max(mx, -uf.data[uf.root(i)]);
  cout << mx << endl;
}
