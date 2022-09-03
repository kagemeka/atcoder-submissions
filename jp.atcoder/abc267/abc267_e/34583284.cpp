#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  vector<long> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  vector<vector<int>> g(n);
  for(int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  vector<long> s(n);
  for(int i = 0; i < n; i++) {
    for(int j: g[i]) s[j] += a[i];
  }
  priority_queue<pair<long, int>> que;
  for(int i = 0; i < n; i++) { que.emplace(-s[i], i); }
  long mn = 0;
  vector<bool> deleted(n);
  while(que.size()) {
    auto [x, u] = que.top();
    que.pop();
    if(deleted[u]) continue;
    deleted[u] = true;
    x = -x;
    mn = max(mn, x);
    for(auto& v: g[u]) {
      s[v] -= a[u];
      if(deleted[v]) continue;
      que.emplace(-s[v], v);
    }
  }
  cout << mn << endl;
}
