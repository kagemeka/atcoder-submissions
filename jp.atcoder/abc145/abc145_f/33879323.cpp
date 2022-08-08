#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, r;
  cin >> n >> r;
  vector<int> h(n + 1);
  for(int i = 0; i < n; i++) cin >> h[i + 1];
  long const inf = 1l << 60;
  vector<vector<long>> dp(n + 1, vector<long>(r + 1, inf));
  dp[0][0] = 0;
  auto diff = [&](int i, int j) { return max(0, h[j] - h[i]); };
  for(int i = 1; i <= n; i++) {
    for(int j = 0; j < i; j++) {
      for(int k = r; k >= 0; k--) {
        dp[i][k] = min(dp[i][k], dp[j][k] + diff(j, i));
        if(k < r) dp[j][k + 1] = dp[j][k];
        dp[j][k] = inf;
      }
    }
  }
  long mn = inf;
  for(int i = 0; i <= n; i++) {
    for(int k = 0; k <= r; k++) { mn = min(mn, dp[i][k]); }
  }
  cout << mn << endl;
}
