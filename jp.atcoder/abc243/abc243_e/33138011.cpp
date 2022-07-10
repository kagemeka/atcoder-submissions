#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  using tup = tuple<int, int, int>;
  vector<tup> edges;
  while(m--) {
    int a, b, c;
    cin >> a >> b >> c;
    a--;
    b--;
    edges.emplace_back(a, b, c);
  }
  long const inf = 1l << 60;
  vector<vector<long>> g(n, vector<long>(n, inf));
  for(int i = 0; i < n; i++) g[i][i] = 0;
  for(auto& [a, b, c]: edges) {
    g[a][b] = c;
    g[b][a] = c;
  }
  for(int k = 0; k < n; k++) {
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < n; j++) { g[i][j] = min(g[i][j], g[i][k] + g[k][j]); }
    }
  }
  int cnt = 0;
  for(auto& [a, b, c]: edges) {
    for(int k = 0; k < n; k++) {
      if(k == a || k == b) continue;
      if(g[a][k] + g[k][b] <= c) {
        cnt++;
        break;
      }
    }
  }
  cout << cnt << endl;
}
