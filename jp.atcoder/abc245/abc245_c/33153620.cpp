#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, k;
  cin >> n >> k;
  vector<int> a(n), b(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  for(int i = 0; i < n; i++) cin >> b[i];
  vector<bool> dp(2, true);
  for(int i = 0; i < n - 1; i++) {
    vector<bool> ndp(2, false);
    ndp[0] = ndp[0] | (dp[0] & (abs(a[i + 1] - a[i]) <= k));
    ndp[0] = ndp[0] | (dp[1] & (abs(a[i + 1] - b[i]) <= k));
    ndp[1] = ndp[1] | (dp[0] & (abs(b[i + 1] - a[i]) <= k));
    ndp[1] = ndp[1] | (dp[1] & (abs(b[i + 1] - b[i]) <= k));
    swap(dp, ndp);
  }
  cout << ((dp[0] | dp[1]) ? "Yes" : "No") << endl;
}
