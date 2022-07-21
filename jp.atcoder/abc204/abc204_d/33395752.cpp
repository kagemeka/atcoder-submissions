#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  // subset sum, reachable
  int const m = 1 << 17;
  int s = 0;
  vector<bool> dp(m);
  dp[0] = true;
  for(auto& x: a) {
    s += x;
    for(int i = m - 1; i >= x; i--) { dp[i] = dp[i] | dp[i - x]; }
  }
  int mn = 1 << 30;
  for(int i = 0; i < m; i++) {
    if(!dp[i]) continue;
    mn = min(mn, max(i, s - i));
  }
  cout << mn << endl;
}
