#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<long> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  long const inf = 1l << 60;
  vector<vector<long>> dp(n + 1, vector<long>(m + 1, -inf));
  // priority_queue<long> a
  dp[0][0] = 0;
  for(int i = 0; i < n; i++) {
    dp[i + 1] = dp[i];
    for(int j = 0; j < m; j++) {
      dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + (j + 1) * a[i]);
    }
  }
  cout << dp[n][m] << endl;
}
