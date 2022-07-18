#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  string s;
  cin >> s;
  vector<int> dp(2);
  dp[1] = 1;
  for(auto& c: s) {
    int d = c - '0';
    vector<int> ndp(2);
    ndp[0] = min(dp[0] + d, dp[1] + 10 - d);
    ndp[1] = min(dp[0] + d + 1, dp[1] + 10 - d - 1);
    swap(dp, ndp);
  }
  cout << dp[0] << endl;
}