
#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  using p = tuple<int, int, int>;
  vector<p> xyz(n);
  for(int i = 0; i < n; i++) {
    int x, y, z;
    cin >> x >> y >> z;
    xyz[i] = {x, y, z};
  }
  vector<vector<int>> g(n, vector<int>(n));
  for(int i = 0; i < n; i++) {
    auto [x, y, z] = xyz[i];
    for(int j = 0; j < n; j++) {
      auto [a, b, c] = xyz[j];
      g[i][j] = abs(x - a) + abs(y - b) + max(0, c - z);
    }
  }
  int const inf = 1 << 30;
  vector<vector<int>> dp(1 << n, vector<int>(n, inf));
  dp[1 << 0][0] = 0;
  for(int s = 0; s < 1 << n; s++) {
    for(int i = 0; i < n; i++) {
      if(s >> i & 1) continue;
      int t = s | (1 << i);
      for(int j = 0; j < n; j++) {
        if(~s >> j & 1) continue;
        dp[t][i] = min(dp[t][i], dp[s][j] + g[j][i]);
      }
    }
  }
  int mn = inf;
  int s = (1 << n) - 1;
  for(int i = 1; i < n; i++) { mn = min(dp[s][i] + g[i][0], mn); }
  cout << mn << endl;
}
