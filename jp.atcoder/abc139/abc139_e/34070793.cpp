#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<vector<int>> a(n, vector<int>(n - 1));
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n - 1; j++) {
      cin >> a[i][j];
      a[i][j]--;
    }
  }
  int n2 = n * n;
  vector<vector<int>> g(n2);
  vector<int> in_deg(n2);
  auto id = [&](int i, int j) -> int {
    if(i > j) swap(i, j);
    return i * n + j;
  };
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n - 2; j++) {
      int u = id(i, a[i][j]);
      int v = id(i, a[i][j + 1]);
      g[u].push_back(v);
      in_deg[v]++;
    }
  }
  int const inf = 1 << 30;
  vector<int> dist(n2, inf);
  queue<int> que;
  for(int i = 0; i < n2; i++) {
    if(in_deg[i] == 0) {
      que.push(i);
      dist[i] = 1;
    }
  }
  while(que.size()) {
    int u = que.front();
    que.pop();
    for(int v: g[u]) {
      in_deg[v]--;
      if(dist[v] == inf || dist[u] + 1 > dist[v]) dist[v] = dist[u] + 1;
      if(!in_deg[v]) que.push(v);
    }
  }
  int res = *max_element(dist.begin(), dist.end());
  cout << (res == inf ? -1 : res) << endl;
}
