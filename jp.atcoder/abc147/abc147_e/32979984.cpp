#include <bits/stdc++.h>

using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  // O((H + W) * 80 * 2 * HW) <= O(4 * 80^4) < 1.5 * 10^8

  int h, w;
  cin >> h >> w;
  vector<vector<int>> a(h, vector<int>(w));

  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      cin >> a[i][j];
    }
  }
  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      int b;
      cin >> b;
      a[i][j] -= b;
    }
  }

  int offset = (h + w) * 80;
  int size = offset * 2 + 2;

  vector<vector<bool>> dp(w + 1, vector<bool>(size));
  dp[0][offset] = true;
  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      for (int k = 0; k < size; k++) {
        dp[j + 1][k] = dp[j + 1][k] | dp[j][k];
      }
      vector<bool> ndp(size);
      int d = abs(a[i][j]);
      for (int k = 0; k < size - d; k++) {
        ndp[k + d] = ndp[k + d] | dp[j + 1][k];
        ndp[k] = ndp[k] | dp[j + 1][k + d];
      }

      swap(dp[j + 1], ndp);
    }
    if (i == 0) dp[0][offset] = false;
  }

  int mn = 1 << 30;
  for (int i = 0; i < size; i++) {
    if (dp[w][i]) mn = min(mn, abs(i - offset));
  }
  cout << mn << endl;
}
