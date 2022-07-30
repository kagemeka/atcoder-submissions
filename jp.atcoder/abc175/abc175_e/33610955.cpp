#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int h, w, k;
  cin >> h >> w >> k;
  vector<vector<int>> v(h, vector<int>(w));
  for(int i = 0; i < k; i++) {
    int y, x, val;
    cin >> y >> x >> val;
    v[y - 1][x - 1] = val;
  }
  vector<vector<long>> dp(w + 1, vector<long>(4));
  for(int i = 0; i < h; i++) {
    for(int j = 0; j < w; j++) {
      for(int k = 2; k >= 0; k--) {
        dp[j + 1][k + 1] = max(dp[j + 1][0] + v[i][j], dp[j][k] + v[i][j]);
        dp[j + 1][k + 1] = max(dp[j + 1][k + 1], dp[j][k + 1]);
      }
    }
    for(int j = 0; j < w + 1; j++) {
      dp[j][0] = *max_element(dp[j].begin(), dp[j].end());
    }
  }
  cout << *max_element(dp[w].begin(), dp[w].end()) << endl;
}
