#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  vector<long> s(n);
  vector<vector<int>> g(n);
  for(int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  for(int i = 0; i < n; i++) {
    for(int j: g[i]) { s[j] += a[i]; }
  }
  auto possible = [&](long x) -> bool {
    auto b = s;
    queue<int> que;
    vector<bool> deleted(n);
    for(int i = 0; i < n; i++) {
      if(b[i] <= x) {
        que.push(i);
        deleted[i] = true;
      }
    }
    while(que.size()) {
      int u = que.front();
      que.pop();
      for(auto& v: g[u]) {
        b[v] -= a[u];
        if(b[v] > x) continue;
        if(deleted[v]) continue;
        deleted[v] = true;
        que.push(v);
      }
    }
    for(int i = 0; i < n; i++) {
      if(!deleted[i]) return false;
    }
    return true;
  };
  long ng = -1;
  long ok = 1l << 60;
  while(ok - ng > 1) {
    long x = (ng + ok) >> 1;
    if(possible(x)) ok = x;
    else ng = x;
  }
  cout << ok << endl;
  // deleted
  // manage surround sum
  // bfs
  // que
  // binary search
}
