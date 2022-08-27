#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  int const K = 1 << 17;
  vector<int> a(K), x(K, -1);
  for(int i = 0; i < n; i++) {
    int t;
    cin >> t;
    cin >> x[t] >> a[t];
  }
  long const inf = 1l << 60;
  vector<vector<long>> dp(K, vector<long>(5, -inf));
  dp[0][0] = 0;
  for(int i = 1; i < K; i++) {
    // not move
    for(int j = 0; j < 5; j++) { dp[i][j] = dp[i - 1][j]; }
    // move
    if(x[i] == -1) continue;
    for(int j = max(i - 5, 0); j < i; j++) {
      for(int k = 0; k < 5; k++) {
        int dx = abs(x[i] - k);
        int dt = i - j;
        if(dt < dx) continue;
        dp[i][x[i]] = max(dp[i][x[i]], dp[j][k] + a[i]);
      }
    }
  }
  long res = 0;
  for(int i = 0; i < 5; i++) { res = max(res, dp[K - 1][i]); }
  cout << res << endl;
}
