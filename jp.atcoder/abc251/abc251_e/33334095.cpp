#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  long const inf = 1l << 60;
  long mn = inf;
  for(int j = 0; j < 2; j++) {
    vector<long> dp(2, inf);
    dp[j] = 0;
    for(int i = 0; i < n; i++) {
      vector<long> ndp(2, inf);
      ndp[0] = dp[1];
      ndp[1] = min(dp[0], dp[1]) + a[i];
      swap(ndp, dp);
    }
    mn = min(mn, dp[j]);
  }
  cout << mn << endl;
}