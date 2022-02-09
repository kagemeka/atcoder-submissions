#include <iostream>


#include <vector>
int main() {
  using namespace std;
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m;
  cin >> n >> m;
  int inf = 1 << 29;
  vector<vector<int>> g(n, vector<int>(n, inf));
  for (int i = 0; i < n; i++) g[i][i] = 0;
  for (int i = 0; i < m; i++) {
    int a, b, t;
    cin >> a >> b >> t;
    a--;  b--;
    g[a][b] = g[b][a] = t;
  }
  for (int k = 0; k < n; k++)  {
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
      }
    }
  }

  int mn = inf;
  for (int i = 0; i < n; i++) {
    int mx = 0;
    for (int j = 0; j < n; j++) {
      mx = max(mx, g[i][j]);
    }
    mn = min(mn, mx);
  }
  cout << mn << '\n';
}
