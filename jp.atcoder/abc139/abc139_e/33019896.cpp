#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;

  int m = n * n;

  vector<vector<int>> a(n, vector<int>(n - 1));
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n - 1; j++) {
      cin >> a[i][j];
      a[i][j]--;
    }
  }

  auto get_id = [&](int u, int v) -> int {
    if(u > v) swap(u, v);
    return u * n + v;
  };

  vector<vector<int>> g(m);
  vector<int> dist(m, -1);
  vector<int> on_stack(m, 0);

  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n - 2; j++) {
      int u = get_id(i, a[i][j]);
      int v = get_id(i, a[i][j + 1]);
      g[v].push_back(u); // rev
    }
  }

  function<bool(int)> dfs;
  dfs = [&](int u) -> bool {
    on_stack[u] = true;
    dist[u] = 0;
    for(auto& v: g[u]) {
      if(on_stack[v]) return false;
      if(dist[v] == -1)
        if(!dfs(v)) return false;
      dist[u] = max(dist[u], dist[v] + 1);
    }
    on_stack[u] = false;
    return true;
  };

  int res = 0;

  for(int i = 0; i < m; i++) {
    if(dist[i] == -1)
      if(!dfs(i)) {
        cout << -1 << endl;
        return 0;
      }
    res = max(res, dist[i]);
  }
  cout << res + 1 << endl;
}