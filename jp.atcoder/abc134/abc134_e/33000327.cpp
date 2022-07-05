#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  // if a_i >= a_j (i < j),
  // we cannot mark both i and j with the same color.
  // otherwise we can.
  // -> longest non increasing sequence.

  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];

  int const inf = 1 << 30;

  vector<int> dp(n, inf);
  reverse(a.begin(), a.end());
  for(int i = 0; i < n; i++) {
    int j = upper_bound(dp.begin(), dp.end(), a[i]) - dp.begin();
    dp[j] = a[i];
  }
  int res = lower_bound(dp.begin(), dp.end(), inf) - dp.begin();
  cout << res << endl;
}
