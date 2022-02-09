#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, m; cin >> n >> m;
  vector<unordered_set<int>> graph(n);
  for (int i = 0; i < m; i++) {
    int a, b; cin >> a >> b; a--; b--;
    graph[a].insert(b); graph[b].insert(a);
  }
  string ans = "IMPOSSIBLE";
  for (auto &x : graph[0]) {
    if (graph[x].find(n - 1) != graph[x].end()) {
      ans = "POSSIBLE"; break;
    }
  }
  cout << ans << '\n';
  return 0;
}
