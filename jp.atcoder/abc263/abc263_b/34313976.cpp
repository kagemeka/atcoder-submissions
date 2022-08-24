#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<vector<int>> g(n);
  for(int i = 1; i < n; i++) {
    int p;
    cin >> p;
    p--;
    g[p].push_back(i);
  }
  vector<int> depth(n);
  queue<int> que;
  que.push(0);
  while(que.size()) {
    int u = que.front();
    que.pop();
    for(int v: g[u]) {
      depth[v] = depth[u] + 1;
      que.push(v);
    }
  }
  cout << depth[n - 1] << endl;
}
