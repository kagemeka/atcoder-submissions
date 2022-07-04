#include <bits/stdc++.h>

using namespace std;

template <typename G>
auto connected_components(const G& g) -> vector<int> {
  int n = g.size();
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
  return labels;
}

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

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

  auto labels = connected_components(g);
  int k = *max_element(labels.begin(), labels.end()) + 1;
  cout << k << endl;
}
