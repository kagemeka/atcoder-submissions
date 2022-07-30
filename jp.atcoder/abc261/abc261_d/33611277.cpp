#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  vector<int> x(n);
  for(int i = 0; i < n; i++) cin >> x[i];
  vector<int> y(n + 1);
  for(int i = 0; i < m; i++) {
    int c, x;
    cin >> c >> x;
    y[c] = x;
  }
  long const inf = 1l << 60;
  vector<long> dp(n + 1, -inf);
  dp[0] = 0;
  for(int i = 0; i < n; i++) {
    long v = 0;
    for(int j = n; j > 0; j--) {
      v = max(v, dp[j]);
      dp[j] = max(dp[j], dp[j - 1] + x[i] + y[j]);
    }
    dp[0] = max(dp[0], v);
  }
  cout << *max_element(dp.begin(), dp.end()) << endl;
}
