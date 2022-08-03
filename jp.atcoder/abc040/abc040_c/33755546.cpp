#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  long const inf = 1l << 60;
  vector<long> dp(n + 1, inf);
  dp[0] = 0;
  for(int i = 0; i < n - 1; i++) {
    for(int d = 1; d <= 2; d++) {
      int j = min(i + d, n - 1);
      dp[j] = min(dp[j], dp[i] + abs(a[j] - a[i]));
    }
  }
  cout << dp[n - 1] << endl;
}
