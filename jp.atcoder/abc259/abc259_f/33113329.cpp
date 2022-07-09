#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> deg(n);
  for(int i = 0; i < n; i++) cin >> deg[i];
  using pi = pair<int, int>;
  vector<vector<pi>> g(n);
  for(int i = 0; i < n - 1; i++) {
    int u, v, w;
    cin >> u >> v >> w;
    u--;
    v--;
    g[u].emplace_back(v, w);
    g[v].emplace_back(u, w);
  }
  function<void(int)> dfs;
  vector<int> parent(n, -1);
  vector<vector<int>> weights(n);
  dfs = [&](int u) {
    for(auto& [v, w]: g[u]) {
      if(v == parent[u]) continue;
      parent[v] = u;
      dfs(v);
      long nw;
      if(deg[v] != 0) {
        nw = w;
      } else {
        nw = weights[v].size() ? w - weights[v][0] : 0;
      }
      if(nw <= 0) continue;
      weights[u].push_back(nw);
    }
    sort(weights[u].begin(), weights[u].end());
    vector<int> new_w;
    for(int i = (int)weights[u].size() - 1; i >= 0; i--) {
      if(deg[u] == 0) break;
      new_w.push_back(weights[u][i]);
      deg[u]--;
    }
    reverse(new_w.begin(), new_w.end());
    swap(weights[u], new_w);
  };
  dfs(0);
  long res = 0;
  for(int i = 0; i < n; i++) {
    for(auto& w: weights[i]) { res += w; }
  }
  cout << res << endl;
}
