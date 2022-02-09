#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, a;
  cin >> n >> a;
  vector<int> x(n);
  for (int i = 0; i < n; i++) {
    cin >> x[i];
  }
  int m = n * *max_element(x.begin(), x.end());
  vector<vector<long long>> dp(n + 1, vector<long long>(m + 1));
  dp[0][0] = true;
  for (int i = 0; i < n; i++) {
    auto ndp = dp;
    for (int j = 1; j <= n; j++) {
      for (int k = x[i]; k <= m; k++) {
        ndp[j][k] += dp[j-1][k-x[i]];
      }
    }
    dp = ndp;
  }
  long long res = 0;
  for (int i = 1; i <= n; i++) res += dp[i][a*i];
  cout << res << '\n';
  return 0;
}
