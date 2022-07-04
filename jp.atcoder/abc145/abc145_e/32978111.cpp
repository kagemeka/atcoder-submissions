#include <bits/stdc++.h>

using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, t;
  cin >> n >> t;

  vector<pair<int, int>> ab(n);
  for (int i = 0; i < n; i++) {
    int a, b;
    cin >> a >> b;
    ab.emplace_back(a, b);
  }

  sort(ab.begin(), ab.end());

  int mx = 0;
  vector<int> dp(t);
  for (auto& [a, b] : ab) {
    for (int i = t - 1; i >= 0; i--) {
      mx = max(mx, dp[i] + b);
      if (i >= a) {
        dp[i] = max(dp[i], dp[i - a] + b);
      }
    }
  }

  cout << mx << endl;
}
