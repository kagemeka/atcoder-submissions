#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, a, b, m;
  cin >> n >> a >> b >> m;
  a--; b--;

  vector<vector<int>> graph(n, vector<int>(n, 0));
  for (int i = 0; i < m; i++) {
    int x, y;
    cin >> x >> y;
    x--; y--;
    graph[x][y] = 1;
    graph[y][x] = 1;
  }

  vector<int> paths(n, 0);
  paths[a] = 1;
  while (!paths[b]) {
    vector<int> nxt(n, 0);
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        nxt[i] += graph[i][j] * paths[j];
      }
    }
    paths = nxt;
  }
  cout << paths[b] << '\n';
  return 0;
}
