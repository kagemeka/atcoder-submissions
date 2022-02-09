#include <bits/stdc++.h>
using namespace std;
long long INF = 1001001001001001;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m;
  cin >> n >> m;
  vector<long long> dist_0(n, INF);
  vector<vector<long long>> dist(n, vector<long long>(n, INF));
  for (int i = 0; i < n; i++) {
    dist[i][i] = 0;
  }
  for (int i = 0; i < m; i++) {
    int u, v, l;
    cin >> u >> v >> l;
    u--; v--;
    if (u > v) swap(u, v);
    if (u == 0) {
      dist_0[v] = l;
    } else {
      dist[u][v] = l;
      dist[v][u] = l;
    }
  }
  for (int k = 0; k < n; k++) {
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
      }
    }
  }
  long long shortest_dist = INF;
  for (int i = 1; i < n - 1; i++) {
    for (int j = i + 1; j < n; j++) {
      shortest_dist = min(shortest_dist, dist_0[i] + dist_0[j] + dist[i][j]);
    }
  }
  if (shortest_dist == INF) {
    cout << -1 << '\n';
  } else {
    cout << shortest_dist << '\n';
  }
  return 0;
}
