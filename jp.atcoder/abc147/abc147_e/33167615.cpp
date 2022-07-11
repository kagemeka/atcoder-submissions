#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  // h * w * (h + w) * max(|a - b|)
  // k = 80
  // 4k^4, 1.6 * 10^8
  // bitset 1/64
  int const k = 80;
  int const offset = 2 * k * k;
  int const size = 2 * offset + 2;
  int h, w;
  cin >> h >> w;
  vector<vector<int>> diff(h, vector<int>(w));
  for(int t = 0; t < 2; t++) {
    for(int i = 0; i < h; i++) {
      for(int j = 0; j < w; j++) {
        int x;
        cin >> x;
        diff[i][j] += pow(-1, t) * x;
      }
    }
  }
  using bits = bitset<size>;
  vector<bits> dp(w + 1);
  dp[0].set(offset);
  for(int i = 0; i < h; i++) {
    for(int j = 0; j < w; j++) {
      dp[j + 1] |= dp[j];
      bits ndp;
      int d = abs(diff[i][j]);
      ndp |= dp[j + 1] << d;
      ndp |= dp[j + 1] >> d;
      swap(dp[j + 1], ndp);
    }
    if(i == 0) dp[0].reset(0);
  }
  int mn = size;
  for(int i = 0; i < size; i++) {
    if(dp[w].test(i)) mn = min(mn, abs(i - offset));
  }
  cout << mn << endl;
}
