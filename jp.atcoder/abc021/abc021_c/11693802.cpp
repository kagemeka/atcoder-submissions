#include <bits/stdc++.h>
using namespace std;
int MOD = 1e9 + 7;
int INF = 1001;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, a, b, m;
  cin >> n >> a >> b >> m;
  a--; b--;

  vector<vector<int>> graph(n, vector<int>(0));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      int u, v;
      cin >> u >> v;
      u--; v--;
      graph[u].push_back(v);
      graph[v].push_back(u);
    }
  }

  queue<int> q;
  q.push(a);
  vector<int> dist(n, INF);
  dist[a] = 0;
  vector<long long> paths(n, 0);
  paths[a] = 1;
  while (!q.empty()) {
    auto u = q.front(); q.pop();
    for (auto &v : graph[u]) {
      if (dist[v] < dist[u] + 1) continue;
      if (dist[v] == INF) q.push(v);
      dist[v] = dist[u] + 1;
      paths[v] += paths[u];
      paths[v] %= MOD;
    }
  }
  cout << paths[b] << '\n';
  return 0;
}
