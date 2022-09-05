#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<vector<int>> lim(n + 1, vector<int>(n, 20));
  for(int i = 0; i < m; i++) {
    int x, y, z;
    cin >> x >> y >> z;
    --y;
    lim[x][y] = min(lim[x][y], z);
  }
  int n2 = 1 << n;
  vector<long> dp(n2);
  dp[0] = 1;
  for(int s = 0; s < n2; s++) {
    bool ok = true;
    vector<int> c(n);
    for(int i = 0; i < n; i++) c[i] = s >> i & 1;
    for(int i = 0; i < n - 1; i++) c[i + 1] += c[i];
    auto z = lim[c[n - 1]];
    for(int i = 0; i < n; i++) { ok = ok && c[i] <= z[i]; }
    if(!ok) {
      dp[s] = 0;
      continue;
    }
    for(int i = 0; i < n; i++) {
      if(s >> i & 1) continue;
      int t = s | 1 << i;
      dp[t] += dp[s];
    }
  }
  cout << dp[n2 - 1] << endl;
}
