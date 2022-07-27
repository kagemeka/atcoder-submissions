#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  cin >> n >> k;
  vector<string> s(n);
  for(int i = 0; i < n; i++) { cin >> s[i]; }
  vector<int> idx(n);
  sort(s.begin(), s.end(), [&](string const& i, string const& j) -> bool {
    return i + j < j + i;
  });
  const string inf = string(1 << 13, 'z');
  vector<string> dp(k + 1, inf);
  dp[0] = "";
  for(int i = n - 1; i >= 0; i--) {
    for(int j = k; j >= 1; j--) { dp[j] = min(dp[j], s[i] + dp[j - 1]); }
  }
  cout << dp[k] << endl;
}
