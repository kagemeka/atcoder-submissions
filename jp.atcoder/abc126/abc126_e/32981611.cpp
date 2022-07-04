#include <bits/stdc++.h>

using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  // z &= 1
  // if z = 1, a_x + a_y is odd, otherwise even.

  // connectivity
  // number of connected components.

  int n, m;
  cin >> n >> m;

  vector<vector<int>> g(n);
  for (int i = 0; i < m; i++) {
    int x, y, z;
    cin >> x >> y >> z;
    x--;
    y--;
    g[x].push_back(y);
    g[y].push_back(x);
  }

  queue<int> que;
  vector<int> labels(n, -1);
  int l = 0;
  for (int i = 0; i < n; i++) {
    if (labels[i] != -1) continue;
    que.push(i);
    while (!que.empty()) {
      int u = que.front();
      que.pop();
      labels[u] = l;
      for (auto& v : g[u]) {
        if (labels[v] == -1) que.push(v);
      }
    }
    l++;
  }
  int k = *max_element(labels.begin(), labels.end()) + 1;
  cout << k << endl;
}
