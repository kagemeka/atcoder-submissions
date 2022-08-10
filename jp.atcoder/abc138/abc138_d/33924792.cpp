#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, q;
  cin >> n >> q;
  vector<vector<int>> g(n);
  for(int i = 0; i < n - 1; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  vector<int> s(n);
  while(q--) {
    int u, x;
    cin >> u >> x;
    u--;
    s[u] += x;
  }
  queue<int> que;
  que.push(0);
  vector<int> parent(n, -1);
  while(que.size()) {
    int u = que.front();
    que.pop();
    for(auto& v: g[u]) {
      if(v == parent[u]) continue;
      parent[v] = u;
      s[v] += s[u];
      que.push(v);
    }
  }
  for(int i = 0; i < n; i++) { cout << s[i] << " \n"[i == n - 1]; }
}
