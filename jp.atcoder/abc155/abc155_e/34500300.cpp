#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s;
  cin >> s;
  vector<int> dp(2), ndp(2);
  dp[1] = 1;
  for(auto& c: s) {
    int d = c - '0';
    ndp[0] = min(dp[0] + d, dp[1] + 10 - d);
    ndp[1] = min(dp[0] + d + 1, dp[1] + 9 - d);
    swap(dp, ndp);
  }
  cout << dp[0] << endl;
}
