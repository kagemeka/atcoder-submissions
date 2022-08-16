#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n), b(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  for(int i = 0; i < n; i++) cin >> b[(i + 1) % n];
  long s = 0;
  for(int i = 0; i < n; i++) s += a[i] + b[i];
  long mx = 0;
  long const inf = 1l << 60;
  for(int t = 0; t < 2; t++) {
    vector<long> dp(2);
    dp[t ^ 1] = -inf;
    for(int i = 0; i < n; i++) {
      vector<long> ndp(2);
      ndp[0] = max(dp[0], dp[1]) + b[i];
      ndp[1] = max(dp[0] + b[i], dp[1]) + a[i];
      swap(dp, ndp);
      // cout << t << ' ' << dp[0] << ' ' << dp[1] << endl;
    }
    mx = max(mx, dp[t]);
  }
  cout << s - mx << endl;
}
