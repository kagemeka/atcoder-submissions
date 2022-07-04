#include <bits/stdc++.h>

using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, t;
  cin >> n >> t;
  const int K = 1 << 13;

  vector<pair<long, int>> dp(K);
  for (int i = 0; i < n; i++) {
    int a, b;
    cin >> a >> b;
    for (int j = K - 1; j >= a; j--) {
      int v = dp[j - a].first + b;
      int w = max(dp[j - a].second, a);
      if (i - w >= t) continue;
      if (v > dp[j].first) {
        dp[j] = {v, w};
      } else if (v == dp[j].first && w > dp[j].second) {
        dp[j].second = w;
      }
    }
  }

  long mx = 0;
  for (int i = 0; i < K; i++) {
    auto [v, w] = dp[i];
    if (i - w < t) mx = max(mx, v);
  }
  cout << mx << endl;
}
