#include <bits/stdc++.h>

using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, m;
  cin >> n >> m;

  vector<int> a(n), b(m);
  for (int i = 0; i < n; i++) cin >> a[i];
  for (int i = 0; i < m; i++) cin >> b[i];

  const int mod = 1000000007;
  vector<int> dp(m + 1, 1);
  for (int i = 0; i < n; i++) {
    for (int j = m - 1; j >= 0; j--) {
      dp[j + 1] -= dp[j] * (a[i] != b[j]);
    }
    for (int j = 0; j < m; j++) {
      dp[j + 1] += dp[j];
      dp[j + 1] %= mod;
    }
    for (int j = 0; j < m + 1; j++) {
      cout << dp[j] << " \n"[j == m];
    }
  }

  cout << dp[m] << endl;
}
