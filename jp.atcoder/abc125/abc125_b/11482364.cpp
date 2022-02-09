#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<int> v(n);
  vector<int> c(n);
  for (int i = 0; i < n; i++) cin >> v[i];
  for (int i = 0; i < n; i++) cin >> c[i];
  int C = accumulate(c.begin(), c.end(), 0);
  vector<vector<int>> dp(n + 1, vector<int>(C + 1));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < C + 1; j++) {
      dp[i+1][j] = dp[i][j];
      if (j - c[i] >= 0) {
        dp[i+1][j] = max(dp[i+1][j], dp[i][j-c[i]] + v[i]);
      }
    }
  }
  int ans = 0;
  for (int i = 0; i < C + 1; i++) {
    ans = max(ans, dp[n][i] - i);
  }
  cout << ans << '\n';
  return 0;
}
