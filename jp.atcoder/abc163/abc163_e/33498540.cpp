#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<long> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  vector<int> idx(n);
  iota(idx.begin(), idx.end(), 0);
  sort(idx.begin(), idx.end(), [&](int i, int j) { return a[i] > a[j]; });
  long const inf = 1l << 60;
  vector<long> dp(n + 1, -inf);
  dp[0] = 0;
  for(int i = 0; i < n; i++) {
    int j = idx[i];
    for(int k = i + 1; k > 0; k--) {
      int l = k - 1;
      int r = (n - 1 - i + k);
      dp[k] = max(dp[k] + a[j] * (r - j), dp[k - 1] + a[j] * (j - l));
    }
    dp[0] = dp[0] + a[j] * (n - 1 - i - j);
  }
  cout << *max_element(dp.begin(), dp.end()) << endl;
}
