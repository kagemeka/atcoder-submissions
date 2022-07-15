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
  // sparse map
  // union by size 1/2*2 + 1/4*4+... = O(N\log{N}) * (O(\log{N} map ops)
  int n, q;
  cin >> n >> q;
  vector<vector<int>> classes(n);
  for(int i = 0; i < n; i++) {
    int c;
    cin >> c;
    c--;
    classes[i].push_back(c);
  }
  union_find uf(n);
  while(q--) {
    int t, x, y;
    cin >> t >> x >> y;
    x--;
    y--;
    if(t == 1) {
      x = uf.root(x);
      y = uf.root(y);
      if(x == y) continue;
      uf.unite(x, y);
      if(classes[x].size() < classes[y].size()) swap(x, y);
      while(classes[y].size()) {
        classes[x].push_back(classes[y].back());
        classes[y].pop_back();
      }
      sort(classes[x].begin(), classes[x].end());
    }
    if(t == 2) {
      x = uf.root(x);
      auto cnt = upper_bound(classes[x].begin(), classes[x].end(), y) -
                 lower_bound(classes[x].begin(), classes[x].end(), y);
      cout << cnt << endl;
    }
  }
}
