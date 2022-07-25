#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> parent(n, -1), in_deg(n);
  for(int i = 0; i < n - 1; i++) {
    int p;
    cin >> p;
    p--;
    parent[i + 1] = p;
    in_deg[p]++;
  }
  vector<int> depth(n, -1);
  queue<int> que;
  for(int i = 0; i < n; i++) {
    if(!in_deg[i]) que.push(i);
  }
  vector<vector<int>> child_deps(n);
  while(que.size()) {
    int u = que.front();
    que.pop();
    sort(child_deps[u].begin(), child_deps[u].end());
    int max_dep = child_deps[u].size();
    int m = max_dep;
    for(int i = 0; i < m; i++) {
      max_dep = max(max_dep, m - i + child_deps[u][i]);
    }
    depth[u] = max_dep;
    int p = parent[u];
    if(p == -1) break;
    child_deps[p].push_back(max_dep);
    if(!--in_deg[p]) que.push(p);
  }
  cout << depth[0] << endl;
}
