#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int s, t, m;
  cin >> s >> t >> m;
  vector<vector<int>> g(s);
  vector<vector<int>> adj(t, vector<int>(t, -1));
  for(int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].push_back(v - s);
  }
  for(int i = 0; i < s; i++) {
    for(auto& j: g[i]) {
      for(auto& k: g[i]) {
        if(j == k) continue;
        int& l = adj[j][k];
        if(l == -1) {
          l = i;
          continue;
        }
        cout << i + 1 << ' ' << j + s + 1 << ' ' << l + 1 << ' ' << k + s + 1
             << endl;
        return 0;
      }
    }
  }
  cout << -1 << endl;
}
