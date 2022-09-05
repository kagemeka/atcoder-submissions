#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  long m;
  cin >> n >> m;
  vector<long> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int const k = 40;
  vector<int> cnt(k);
  for(auto& x: a) {
    for(int i = 0; i < k; i++) cnt[i] += x >> i & 1;
  }
  long const inf = 1l << 60;
  vector<long> dp(2, -inf);
  // x is (just, less than) m
  dp[0] = 0;
  for(int i = k - 1; i >= 0; i--) {
    vector<long> ndp(2, -inf);
    int c = cnt[i];
    ndp[1] = dp[1] + (1l << i) * max(c, n - c);
    if(m >> i & 1) {
      ndp[0] = dp[0] + (1l << i) * (n - c);
      ndp[1] = max(ndp[1], dp[0] + (1l << i) * c);
    } else {
      ndp[0] = dp[0] + (1l << i) * c;
    }
    swap(dp, ndp);
  }
  cout << max(dp[0], dp[1]) << endl;
}
