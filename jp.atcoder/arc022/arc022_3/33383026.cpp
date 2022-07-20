#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<vector<int>> g(n);
  for(int i = 0; i < n - 1; i++) {
    int a, b;
    cin >> a >> b;
    a--;
    b--;
    g[a].push_back(b);
    g[b].push_back(a);
  }
  auto bfs = [&](int u) -> vector<int> {
    vector<int> depth(n, -1);
    depth[u] = 0;
    queue<int> que;
    que.push(u);
    while(que.size()) {
      int u = que.front();
      que.pop();
      for(int v: g[u]) {
        if(depth[v] != -1) continue;
        depth[v] = depth[u] + 1;
        que.push(v);
      }
    }
    return depth;
  };
  int u = 0;
  vector<int> res(2);
  for(int j = 0; j < 2; j++) {
    auto dep = bfs(u);
    int mx = 0;
    for(int i = 0; i < n; i++) {
      if(dep[i] <= mx) continue;
      mx = dep[i];
      u = i;
    }
    res[j] = u;
  }
  cout << res[0] + 1 << ' ' << res[1] + 1 << endl;
}
