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
  auto size_of(int u) -> int { return -data[root(u)]; }
};
auto main() -> int {
  int m = 4;
  int n = m * m;
  // vector<vector<int>> a(m, vector<int>(m));
  int s0 = 0;
  for(int i = 0; i < m; i++) {
    for(int j = 0; j < m; j++) {
      // cin >> a[i][j];
      int x;
      cin >> x;
      int u = i * m + j;
      if(x) s0 |= 1 << u;
    }
  }
  m += 2;
  auto is_ok = [&](int s) -> bool {
    auto id = [&](int i, int j) -> int { return i * m + j; };
    auto dec = [&](int i) -> pair<int, int> {
      return {i / (m - 2), i % (m - 2)};
    };
    if((s & s0) != s0) return false;
    vector<vector<bool>> a(m, vector<bool>(m));
    int cnt = 0;
    for(int u = 0; u < n; u++) {
      if(~s >> u & 1) continue;
      auto [i, j] = dec(u);
      a[i + 1][j + 1] = true;
      cnt++;
    }
    auto on_grid = [&](int i, int j) -> bool {
      return 0 <= i && i < m && 0 <= j && j < m;
    };
    // cerr << 1 << endl;
    union_find uf(n + 20);
    vector<int> dy = {-1, 0, 1, 0}, dx = {0, -1, 0, 1};
    for(int i = 0; i < m; i++) {
      for(int j = 0; j < m; j++) {
        int u = id(i, j);
        for(int k = 0; k < 4; k++) {
          int ni = i + dy[k];
          int nj = j + dx[k];
          if(!on_grid(ni, nj)) continue;
          if(a[ni][nj] == a[i][j]) {
            int v = id(ni, nj);
            uf.unite(u, v);
          }
        }
      }
    }
    auto [p, q] = dec(__builtin_ctz(s));
    int x = uf.size_of(0);
    int y = uf.size_of(id(p + 1, q + 1));
    // cout << x << ' ' << y << ' ' << cnt << endl;
    return x == n + 20 - cnt && y == cnt;
  };
  // cerr << 1 << endl;
  int res = 0;
  for(int s = 1; s < 1 << n; s++) { res += is_ok(s); }
  cout << res << endl;
}
