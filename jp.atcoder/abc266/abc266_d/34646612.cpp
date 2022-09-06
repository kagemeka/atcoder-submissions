#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  long const inf = 1l << 60;
  int m = 5;
  int const T = 1 << 17;
  vector<vector<long>> a(T, vector<long>(m, 0));
  for(int i = 0; i < n; i++) {
    int t, x, y;
    cin >> t >> x >> y;
    a[t][x] = y;
  }
  vector<long> dp(m, -inf);
  dp[0] = 0;
  for(int i = 0; i < T - 1; i++) {
    vector<long> ndp(m, -inf);
    for(int j = 0; j < m; j++) {
      for(int d = -1; d < 2; d++) {
        int k = j + d;
        if(k < 0 || m <= k) continue;
        ndp[k] = max(ndp[k], dp[j] + a[i + 1][k]);
      }
    }
    swap(dp, ndp);
  }
  cout << *max_element(dp.begin(), dp.end()) << endl;
  ;
}
