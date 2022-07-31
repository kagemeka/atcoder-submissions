#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  int n;
  cin >> n;
  string ns = to_string(n);
  vector<vector<int>> dp(2, vector<int>(8));
  dp[0][0] = 1;
  vector<int> v{3, 5, 7};
  for(auto& c: ns) {
    int d = c - '0';
    vector<vector<int>> ndp(2, vector<int>(8));
    for(int i = 0; i < 2; i++) {
      for(int s = 0; s < 8; s++) {
        for(int j = 0; j < 3; j++) {
          int ni = i | (v[j] < d), ns = s | 1 << j;
          if(!i && v[j] > d) continue;
          ndp[ni][ns] += dp[i][s];
        }
        if(!s) { ndp[1][0] = 1; }
      }
    }
    swap(dp, ndp);
  }
  cout << dp[0][7] + dp[1][7] << endl;
}
