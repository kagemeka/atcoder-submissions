#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int const inf = 1 << 30;
  vector<int> idx(n);
  iota(idx.begin(), idx.end(), 0);
  sort(idx.begin(), idx.end(), [&](int i, int j) { return a[i] < a[j]; });
  int mx = -inf;
  vector<int> state(n, 0);
  vector<vector<int>> g(n);
  while(m--) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].push_back(v);
  }
  queue<int> que;
  for(int i: idx) {
    if(state[i] == 1) continue;
    que.push(i);
    while(que.size()) {
      int u = que.front();
      que.pop();
      for(int v: g[u]) {
        if(state[v] == 1) continue;
        state[v] = 1;
        que.push(v);
        mx = max(mx, a[v] - a[i]);
      }
    }
  }
  cout << mx << endl;
}
