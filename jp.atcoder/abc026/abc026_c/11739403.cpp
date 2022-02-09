#include <bits/stdc++.h>
using namespace std;

int dfs(int x, vector<unordered_set<int>> &graph) {
  if (graph[x].empty()) return 1;
  vector<int> salaries(0);
  for (int y : graph[x]) {
    salaries.push_back(dfs(y, graph));
  }
  sort(salaries.begin(), salaries.end());
  return salaries[0] + salaries[salaries.size()-1] + 1;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n;
  cin >> n;
  vector<unordered_set<int>> graph(n);
  for (int i = 1; i < n; i++) {
    int b;
    cin >> b;
    b--;
    graph[b].insert(i);
  }
  int res = dfs(0, graph);
  cout << res << '\n';
  return 0;
}
