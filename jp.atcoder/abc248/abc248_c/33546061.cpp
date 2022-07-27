#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m, k;
  cin >> n >> m >> k;
  int const mod = 998244353;
  vector<int> dp(k + 1, 0);
  dp[0] = 1;
  auto get = [&](int i) -> int {
    if(i < 0) return 0;
    return dp[i];
  };
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < k; j++) {
      dp[j + 1] += dp[j];
      dp[j + 1] %= mod;
    }
    for(int j = k; j >= 0; j--) {
      dp[j] = get(j - 1) - get(j - 1 - m);
      dp[j] %= mod;
    }
  }
  int res = 0;
  for(auto& x: dp) {
    res += x;
    res %= mod;
  }
  res = (res + mod) % mod;
  cout << res << endl;
}
