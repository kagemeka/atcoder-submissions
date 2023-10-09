#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  string s;
  cin >> s;
  int n = s.size();

  vector<int> dp(n + 2);
  dp[0] = -1;
  dp[1] = 1;
  for(int i = 1; i < n; i++) {
    if(s[i] == s[i - 1]) {
      dp[i + 2] = dp[i - 1] + 2;
    } else {
      dp[i + 2] = dp[i + 1] + 1;
    }
  }
  cout << dp[n + 1] << endl;
}
