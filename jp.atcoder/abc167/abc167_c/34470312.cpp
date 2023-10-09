#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m, x;
  cin >> n >> m >> x;
  int n2 = 1 << n;
  vector<int> c(n);
  vector<vector<int>> a(n, vector<int>(m));
  for(int i = 0; i < n; i++) {
    cin >> c[i];
    for(int j = 0; j < m; j++) cin >> a[i][j];
  }
  int const inf = 1 << 30;
  int mn = inf;
  for(int s = 1; s < n2; s++) {
    vector<int> score(m);
    int cost = 0;
    for(int i = 0; i < n; i++) {
      if(~s >> i & 1) continue;
      for(int j = 0; j < m; j++) score[j] += a[i][j];
      cost += c[i];
    }
    bool ok = true;
    for(auto& v: score) {
      if(v >= x) continue;
      ok = false;
      break;
    }
    if (ok) mn = min(mn, cost);
  }
  cout << (mn == inf ? -1 : mn) << endl;
}
