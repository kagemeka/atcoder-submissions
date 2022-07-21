#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, ma, mb;
  cin >> n >> ma >> mb;
  int const inf = 1 << 30;
  int const k = 1 << 9;
  vector<vector<int>> dp(k, vector<int>(k, inf));
  dp[0][0] = 0;
  while(n--) {
    int a, b, c;
    cin >> a >> b >> c;
    for(int i = k - 1; i >= a; i--) {
      for(int j = k - 1; j >= b; j--) {
        dp[i][j] = min(dp[i][j], dp[i - a][j - b] + c);
      }
    }
  }
  int mn = inf;
  for(int i = 1; i < k / max(ma, mb); i++) {
    mn = min(mn, dp[i * ma][i * mb]);
  }
  cout << (mn == inf ? -1 : mn) << endl;
}
