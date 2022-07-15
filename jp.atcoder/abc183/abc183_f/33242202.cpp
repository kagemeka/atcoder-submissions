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
  vector<map<int, int>> classes(n);
  for(int i = 0; i < n; i++) {
    int c;
    cin >> c;
    c--;
    classes[i][c]++;
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
      if(uf.root(x) == y) swap(x, y);
      for(auto& [i, c]: classes[y]) { classes[x][i] += c; }
    }
    if(t == 2) {
      x = uf.root(x);
      cout << classes[x][y] << endl;
    }
  }
}
