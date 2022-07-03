#include <bits/stdc++.h>

using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  const int K = 1 << 17;
  const int K2 = K << 1;
  vector<vector<int>> g(K2);

  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    int x, y;
    cin >> x >> y;
    y += K;
    g[x].push_back(y);
    g[y].push_back(x);
  }

  vector<int> labels(K2, -1);
  function<void(int, int)> dfs;
  dfs = [&](int u, int l) {
    labels[u] = l;
    for (auto& v : g[u]) {
      if (labels[v] != -1) continue;
      dfs(v, l);
    }
  };

  int label = 0;
  for (int i = 0; i < K2; i++) {
    if (labels[i] != -1) continue;
    dfs(i, label);
    label++;
  }
  int k = *max_element(labels.begin(), labels.end()) + 1;
  vector<vector<int>> c(k);
  for (int i = 0; i < K2; i++) {
    c[labels[i]].push_back(i);
  }

  long cnt = 0;
  for (auto& d : c) {
    int x = 0, y = 0;
    for (auto& i : d) {
      if (i < K) x++;
      else y++;
    }
    cnt += (long)x * y;
  }
  cout << cnt - n << endl;
}
