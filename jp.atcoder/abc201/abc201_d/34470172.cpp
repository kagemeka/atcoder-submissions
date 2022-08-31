#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int h, w;
  cin >> h >> w;
  vector<vector<int>> a(h, vector<int>(w));
  for(int i = 0; i < h; i++) {
    string s;
    cin >> s;
    for(int j = 0; j < w; j++) {
      int p = (i + j) & 1;
      // odd: first
      if((p & 1) ^ (s[j] == '+')) {
        a[i][j] = -1;
      } else {
        a[i][j] = 1;
      }
    }
  }
  int const inf = 1 << 30;
  vector<int> dp(w);
  for(int i = h - 1; i >= 0; i--) {
    vector<int> ndp(w);
    for(int j = w - 1; j >= 0; j--) {
      if(i == h - 1 && j == w - 1) continue;
      if((i + j) & 1) {
        // second turn.
        ndp[j] = inf;
        if(i < h - 1) { ndp[j] = min(ndp[j], dp[j] + a[i + 1][j]); }
        if(j < w - 1) { ndp[j] = min(ndp[j], ndp[j + 1] + a[i][j + 1]); }
      } else {
        ndp[j] = -inf;
        if(i < h - 1) { ndp[j] = max(ndp[j], dp[j] + a[i + 1][j]); }
        if(j < w - 1) { ndp[j] = max(ndp[j], ndp[j + 1] + a[i][j + 1]); }
      }
    }
    swap(dp, ndp);
  }
  int s = dp[0];
  cout << (s > 0 ? "Takahashi" : s < 0 ? "Aoki" : "Draw") << endl;
}
