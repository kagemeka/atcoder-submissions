#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n), b(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  for(int i = 0; i < n; i++) cin >> b[(i + 1) % n];
  long s = 0;
  for(int i = 0; i < n; i++) s += a[i] + b[i];
  long mx = 0;
  long const inf = 1l << 60;
  // same /or not, connect/or not
  for(int u = 0; u < 2; u++) {
    for(int v = 0; v < 2; v++) {
      vector<vector<long>> dp(2, vector<long>(2, -inf));
      if(u == 1 && v == 1) continue; // same & connect -> impossible
      dp[u][v] = 0;
      for(int i = 0; i < n; i++) {
        vector<vector<long>> ndp(2, vector<long>(2, -inf));
        ndp[0][0] = max(max(dp[0][0], dp[0][1]), dp[1][0] + b[i]);
        ndp[0][1] = ndp[0][0] + a[i];
        ndp[1][0] = max(max(dp[0][0], dp[0][1]) + b[i], dp[1][0]);
        swap(dp, ndp);
        // cout << u << ' ' << v << " a" << endl;
        // for(int i = 0; i < 2; i++) {
        //   for(int j = 0; j < 2; j++) { cout << dp[i][j] << ' '; }
        // }
        // cout << "\n\n";
      }
      mx = max(mx, dp[u][v]);
    }
  }
  cout << s - mx << endl;
}
