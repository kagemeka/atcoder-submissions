#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  vector<set<int>> g(n);
  while(m--) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].insert(v);
    g[v].insert(u);
  }
  int cnt = 0;
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < i; j++) {
      for(int k = 0; k < j; k++) {
        bool ok = true;
        ok = ok && g[i].count(j) > 0;
        ok = ok && g[j].count(k) > 0;
        ok = ok && g[k].count(i) > 0;
        cnt += ok;
      }
    }
  }
  cout << cnt << endl;
}
