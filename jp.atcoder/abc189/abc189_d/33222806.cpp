#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<bool> is_and(n);
  for(int i = 0; i < n; i++) {
    string s;
    cin >> s;
    is_and[i] = s == "AND";
  }
  vector<long> dp(2, 1);
  for(int i = 0; i < n; i++) {
    vector<long> ndp(2);
    if(is_and[i]) {
      ndp[0] = dp[0] * 2 + dp[1];
      ndp[1] = dp[1];
    } else {
      ndp[0] = dp[0];
      ndp[1] = dp[0] + dp[1] * 2;
    }
    swap(dp, ndp);
  }
  cout << dp[1] << endl;
}
