#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, ma, mb;
  cin >> n >> ma >> mb;
  int const k = 1 << 9;
  int const inf = 1 << 30;
  vector<vector<int>> dp(k, vector<int>(k, inf));
  dp[0][0] = 0;
  while(n--) {
    int a, b, c;
    cin >> a >> b >> c;
    for(int i = k - 1; i >= a; i--) {
      for(int j = b; j < k; j++) {
        dp[i][j] = min(dp[i][j], dp[i - a][j - b] + c);
      }
    }
  }
  int mn = inf;
  for(int i = 1; i <= min((k - 1) / ma, (k - 1) / mb); i++) {
    mn = min(mn, dp[i * ma][i * mb]);
  }
  cout << (mn == inf ? -1 : mn) << endl;
}
