#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m;
  cin >> n >> m;
  vector<vector<int>> graph(n);
  for (int i = 0; i < m; i++) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    graph[a].push_back(b);
    graph[b].push_back(a);
  }
  vector<pair<int, int>> stack;
  stack.push_back(pair<int, int>(0, 0));
  int paths = 0;
  while (!stack.empty()) {
    auto tmp = stack.back(); stack.pop_back();
    int i = tmp.first;
    int visited = tmp.second;
    visited |= 1 << i;
    if (visited == (1 << n) - 1) {
      paths++;
      continue;
    }
    for (int &j : graph[i]) {
      if (visited >> j & 1) continue;
      stack.push_back(pair<int, int>(j, visited));
    }
  }
  cout << paths << '\n';
  return 0;
}
