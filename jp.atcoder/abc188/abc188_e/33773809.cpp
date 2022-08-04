#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  vector<int> order(n);
  iota(order.begin(), order.end(), 0);
  sort(order.begin(), order.end(), [&](int i, int j) { return a[i] < a[j]; });
  vector<vector<int>> g(n);
  for(int i = 0; i < m; i++) {
    int x, y;
    cin >> x >> y;
    x--;
    y--;
    g[x].push_back(y);
  }
  long const inf = 1l << 31;
  long mx = -inf;
  queue<int> que;
  vector<bool> to_que(n);
  for(auto& i: order) {
    if(to_que[i]) continue;
    que.push(i);
    while(que.size()) {
      int u = que.front();
      que.pop();
      if(u != i) { mx = max(mx, (long)a[u] - a[i]); }
      for(auto& v: g[u]) {
        if(to_que[v]) continue;
        to_que[v] = true;
        que.push(v);
      }
    }
  }
  cout << mx << endl;
}
