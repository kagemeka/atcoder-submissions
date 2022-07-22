#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int const k = 1 << 18;
  vector<long> cnt(k);
  for(auto& x: a) cnt[x]++;
  vector<long> dp(4);
  dp[0] = 1;
  for(auto& c: cnt) {
    for(int i = 3; i >= 1; i--) { dp[i] += dp[i - 1] * c; }
  }
  cout << dp[3] << endl;
}
