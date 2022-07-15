#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int const inf = 1 << 30;
  int n, x, y;
  cin >> n >> x >> y;
  vector<vector<int>> dp(x + 1, vector<int>(y + 1, inf));
  dp[0][0] = 0;
  while(n--) {
    int a, b;
    cin >> a >> b;
    for(int i = x; i >= 0; i--) {
      int ni = min(x, i + a);
      for(int j = y; j >= 0; j--) {
        int nj = min(y, j + b);
        dp[ni][nj] = min(dp[ni][nj], dp[i][j] + 1);
      }
    }
  }
  int res = dp[x][y];
  cout << (res == inf ? -1 : res) << endl;
}
