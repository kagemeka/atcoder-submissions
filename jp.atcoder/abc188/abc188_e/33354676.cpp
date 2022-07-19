#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  // bfs
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int const inf = 1 << 30;
  int mx = -inf;
  vector<int> in_deg(n);
  vector<vector<int>> g(n);
  while(m--) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].push_back(v);
    in_deg[v] += 1;
  }
  queue<int> que;
  for(int i = 0; i < n; i++) {
    if(in_deg[i] == 0) que.push(i);
  }
  vector<int> pre_mn(n, inf);
  while(que.size()) {
    int u = que.front();
    que.pop();
    if(pre_mn[u] != inf) { mx = max(mx, a[u] - pre_mn[u]); }
    for(auto& v: g[u]) {
      pre_mn[v] = min(pre_mn[v], min(pre_mn[u], a[u]));
      in_deg[v]--;
      if(in_deg[v] == 0) que.push(v);
    }
  }
  cout << mx << endl;
}
