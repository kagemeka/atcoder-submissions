#include <bits/stdc++.h>

using namespace std;

template <typename G>
auto connected_components(const G& g) -> vector<int> {
  int n = g.size();
  vector<int> labels(n, -1);
  int l = 0;
  function<void(int)> dfs;
  dfs = [&](int u) {
    labels[u] = l;
    for (auto& v : g[u]) {
      if (labels[v] != -1) continue;
      dfs(v);
    }
  };
  for (int i = 0; i < n; i++) {
    if (labels[i] != -1) continue;
    dfs(i);
    l++;
  }
  return labels;
}

auto labels_to_components(const vector<int>& labels) -> vector<vector<int>> {
  int n = labels.size();
  int k = *max_element(labels.begin(), labels.end()) + 1;
  vector<vector<int>> comp(k);
  for (int i = 0; i < n; i++) comp[labels[i]].push_back(i);
  return comp;
}

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

  auto c = labels_to_components(connected_components(g));

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
