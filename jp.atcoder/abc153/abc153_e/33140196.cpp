#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int h, n;
  cin >> h >> n;
  int const inf = 1 << 30;
  vector<int> dp(h + 1, inf);
  dp[0] = 0;
  while(n--) {
    int v, w;
    cin >> v >> w;
    for(int i = 0; i < h; i++) {
      int j = min(h, i + v);
      dp[j] = min(dp[j], dp[i] + w);
    }
  }
  cout << dp[h] << endl;
}
