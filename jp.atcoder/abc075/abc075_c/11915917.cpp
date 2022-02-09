#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, m;
  cin >> n >> m;
  vector<unordered_set<int>> graph(n, unordered_set<int>());
  for (int i = 0; i < m; i++) {
    int a, b; cin >> a >> b; a--; b--;
    graph[a].insert(b);
    graph[b].insert(a);
  }
  int bridges = 0;
  vector<int> stack(0);
  for (int i = 0; i < n; i++) {
    if (graph[i].size() == 1) stack.push_back(i);
  }
  while (!stack.empty()) {
    int x = stack.back(); stack.pop_back();
    for (auto y : graph[x]) {
      bridges++;
      graph[y].erase(x);
      if (graph[y].size() == 1) stack.push_back(y);
    }
  }
  cout << bridges << '\n';
  return 0;
}
