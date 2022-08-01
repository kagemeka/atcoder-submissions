#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string n;
  cin >> n;
  vector<long> dp(2);
  dp[0] = 1;
  long const mod = 1000000007;
  for(auto& c: n) {
    vector<long> ndp(2);
    int d = c - '0';
    ndp[1] += dp[1] * 3;
    ndp[0] = dp[0];
    if(d == 1) {
      ndp[1] += dp[0];
      ndp[0] += dp[0];
    }
    ndp[0] %= mod;
    ndp[1] %= mod;
    swap(dp, ndp);
  }
  cout << (dp[0] + dp[1]) % mod << endl;
}
