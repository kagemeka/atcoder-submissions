#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int h, w;
  cin >> h >> w;
  vector<int> row_cost(h), col_cost(w);
  for(int i = 0; i < h; i++) cin >> row_cost[i];
  for(int j = 0; j < w; j++) cin >> col_cost[j];
  using vl = vector<long>;
  using vvl = vector<vl>;
  using vvvl = vector<vvl>;
  using vvvvl = vector<vvvl>;
  long const inf = 1l << 60;
  vvvvl dp(h, vvvl(w, vvl(2, vl(2, inf))));
  dp[0][0][0][0] = 0;
  dp[0][0][1][0] = row_cost[0];
  dp[0][0][0][1] = col_cost[0];
  dp[0][0][1][1] = row_cost[0] + col_cost[0];
  vector<string> a(h);
  for(int i = 0; i < h; i++) cin >> a[i];
  for(int i = 0; i < h; i++) {
    for(int j = 0; j < w; j++) {
      if(i == 0 && j == 0) continue;
      // from upper
      if(i >= 1) {
        for(int x = 0; x < 2; x++) {
          for(int y = 0; y < 2; y++) {
            int ny = y ^ (a[i - 1][j] != a[i][j]);
            dp[i][j][ny][x] = min(
              dp[i][j][ny][x], dp[i - 1][j][y][x] + (ny == 1 ? row_cost[i] : 0)
            );
          }
        }
      }
      if(j >= 1) {
        for(int y = 0; y < 2; y++) {
          for(int x = 0; x < 2; x++) {
            int nx = x ^ (a[i][j - 1] != a[i][j]);
            dp[i][j][y][nx] = min(
              dp[i][j][y][nx], dp[i][j - 1][y][x] + (nx == 1 ? col_cost[j] : 0)
            );
          }
        }
      }
    }
  }
  long res = inf;
  for(int i = 0; i < 2; i++) {
    for(int j = 0; j < 2; j++) { res = min(res, dp[h - 1][w - 1][i][j]); }
  }
  cout << res << endl;
}
