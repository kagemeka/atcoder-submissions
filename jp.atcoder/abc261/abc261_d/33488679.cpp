#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<long> a(n), b(n + 1);
  for(int i = 0; i < n; i++) cin >> a[i];
  for(int i = 0; i < m; i++) {
    int c, x;
    cin >> c >> x;
    b[c] += x;
  }
  long const inf = 1l << 60;
  vector<long> dp(n + 1, -inf);
  dp[0] = 0;
  for(int i = 0; i < n; i++) {
    long tmp = 0;
    for(int j = 0; j < n + 1; j++) { tmp = max(tmp, dp[j]); }
    for(int j = n; j >= 1; j--) { dp[j] = max(dp[j], dp[j - 1] + a[i] + b[j]); }
    dp[0] = tmp;
  }
  long res = *max_element(dp.begin(), dp.end());
  cout << res << endl;
}
