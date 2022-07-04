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

  const int offset = 2 * 80 * 80;
  const int size = offset * 2 + 2;

  using bits = bitset<size>;

  vector<bits> dp(w + 1);
  dp[0].set(offset);
  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      dp[j + 1] |= dp[j];
      bits ndp;
      int d = abs(a[i][j]);
      ndp |= dp[j + 1] >> d;
      ndp |= dp[j + 1] << d;
      swap(dp[j + 1], ndp);
    }
    if (i == 0) dp[0].reset(offset);
  }

  int mn = 1 << 30;
  for (int i = 0; i < size; i++) {
    if (dp[w][i]) mn = min(mn, abs(i - offset));
  }
  cout << mn << endl;
}
