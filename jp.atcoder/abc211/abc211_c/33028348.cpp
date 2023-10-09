#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  string s;
  cin >> s;
  int n = s.size();

  string t = "chokudai";
  int m = t.size();

  int const mod = 1000000007;

  vector<int> dp(m + 1);
  dp[0] = 1;

  for(int i = 0; i < n; i++) {
    for(int j = 0; j < m; j++) {
      if(s[i] != t[j]) continue;
      dp[j + 1] += dp[j];
      dp[j + 1] %= mod;
    }
  }
  cout << dp[m] << endl;
}
