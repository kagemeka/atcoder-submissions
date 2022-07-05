#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  string s;
  cin >> s;

  int const mod = 1000000007;

  vector<long> dp(4);
  dp[0] = 1;
  for(auto& c: s) {
    if(c == '?') {
      for(int i = 3; i > 0; i--) {
        dp[i] *= 3;
        dp[i] += dp[i - 1];
      }
      dp[0] *= 3;
    } else dp[c - 'A' + 1] += dp[c - 'A'];
    for(int i = 0; i < 4; i++) dp[i] %= mod;
  }
  cout << dp[3] << endl;
}
