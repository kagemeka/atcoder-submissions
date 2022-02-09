#include <bits/stdc++.h>

using namespace std;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int mod = (int)1e9 + 7;

  int n, m; cin >> n >> m;

  vector<vector<int>> edges(n);

  while (m--) {
    int a, b; cin >> a >> b;
    --a, --b;
    edges[a].push_back(b);
    edges[b].push_back(a);
  }

  int inf = 1 << 30;
  vector<int> dist(n, inf);
  dist[0] = 0;

  vector<int> paths(n, 0);
  paths[0] = 1;
  queue<int> q;
  q.push(0);

  while (!q.empty()) {
    int u = q.front();
    q.pop();
    for (int v: edges[u]) {
      int dv = dist[u] + 1;
      if (dv > dist[v]) {
        continue;
      }
      if (dv == dist[v]) {
        paths[v] += paths[u];
        paths[v] %= mod;
        continue;
      }
      paths[v] = paths[u];
      dist[v] = dv;
      q.push(v);
    }
  }
  cout << paths[n - 1] << '\n';
}
