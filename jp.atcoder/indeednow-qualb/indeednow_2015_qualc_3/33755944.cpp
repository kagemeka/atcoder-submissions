#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<vector<int>> g(n);
  for(int i = 0; i < n - 1; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  priority_queue<int> que;
  que.push(0);
  vector<bool> to_que(n);
  to_que[0] = true;
  vector<int> res;
  while(que.size()) {
    int u = que.top();
    que.pop();
    u = -u;
    res.push_back(u);
    for(auto& v: g[u]) {
      if(to_que[v]) continue;
      to_que[v] = true;
      que.push(-v);
    }
  }
  for(int i = 0; i < n; i++) { cout << res[i] + 1 << " \n"[i == n - 1]; }
}
