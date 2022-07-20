#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  long x, y;
  cin >> n >> x >> y;
  vector<long> a(n), b(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  for(int i = 0; i < n; i++) cin >> b[i];
  long const inf = 1l << 60;
  vector<long> dp(1 << n, inf);
  dp[0] = 0;
  for(int s = 0; s < 1 << n; s++) {
    vector<int> que;
    int j = 0;
    for(int i = 0; i < n; i++) {
      if(s >> i & 1) {
        j++;
      } else {
        que.push_back(i);
      }
    }
    for(int i = 0; i < (int)que.size(); i++) {
      long v = abs(b[j] - a[que[i]]) * x + i * y;
      int t = s | (1 << que[i]);
      dp[t] = min(dp[t], dp[s] + v);
    }
  }
  cout << dp[(1 << n) - 1] << endl;
}
