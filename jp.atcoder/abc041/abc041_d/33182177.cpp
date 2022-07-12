#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  vector<int> g(n);
  while(m--) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u] |= 1 << v;
  }
  vector<long> dp(1 << n);
  dp[0] = 1;
  for(int s = 0; s < 1 << n; s++) {
    for(int i = 0; i < n; i++) {
      if(s >> i & 1 || g[i] & s) continue;
      dp[s | 1 << i] += dp[s];
    }
  }
  cout << dp[(1 << n) - 1] << endl;
}
