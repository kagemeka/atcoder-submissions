
#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  vector<int> cost(m);
  vector<int> keys(m);
  for(int i = 0; i < m; i++) {
    cin >> cost[i];
    int b;
    cin >> b;
    for(int j = 0; j < b; j++) {
      int c;
      cin >> c;
      keys[i] |= 1 << (c - 1);
    }
  }
  int const inf = 1 << 30;
  vector<int> dp(1 << n, inf);
  dp[0] = 0;
  for(int i = 0; i < n; i++) {
    for(int t = (1 << n) - 1; t >= 0; t--) {
      dp[t] = min(dp[t], dp[t & ~keys[i]] + cost[i]);
    }
  }
  int res = dp[(1 << n) - 1];
  cout << (res == inf ? -1 : res) << endl;
}
