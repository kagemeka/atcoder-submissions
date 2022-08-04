#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, t;
  cin >> n >> t;
  using pi = pair<int, int>;
  vector<pi> ab(n);
  for(int i = 0; i < n; i++) cin >> ab[i].first >> ab[i].second;
  sort(ab.begin(), ab.end());
  vector<int> dp(t + 1);
  for(auto& [a, b]: ab) {
    for(int i = t - 1; i >= 0; i--) {
      int j = min(t, i + a);
      dp[j] = max(dp[j], dp[i] + b);
    }
  }
  cout << dp[t] << endl;
}
