#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  vector<int> g(n);
  for(int i = 0; i < m; i++) {
    int x, y;
    cin >> x >> y;
    x--;
    y--;
    g[x] |= 1 << y;
  }
  vector<long> dp(1 << n);
  dp[0] = 1;
  for(int s = 0; s < 1 << n; s++) {
    for(int i = 0; i < n; i++) {
      dp[s | 1 << i] += (~s >> i & 1 && !(g[i] & s)) * dp[s];
    }
  }
  cout << dp[(1 << n) - 1] << endl;
}
