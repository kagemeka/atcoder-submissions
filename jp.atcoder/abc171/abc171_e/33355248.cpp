#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  auto dp = [&](vector<int> a) -> vector<int> {
    vector<int> dp(n + 1);
    for(int i = 0; i < n; i++) dp[i + 1] = dp[i] ^ a[i];
    return dp;
  };
  auto dp_l = dp(a);
  reverse(a.begin(), a.end());
  auto dp_r = dp(a);
  for(int i = 0; i < n; i++) {
    cout << (dp_l[i] ^ dp_r[n - 1 - i]) << " \n"[i == n - 1];
  }
}
