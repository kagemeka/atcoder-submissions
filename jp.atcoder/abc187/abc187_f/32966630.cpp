#include <bits/stdc++.h>

using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, m;
  cin >> n >> m;
  vector<int> g(n);
  while (m--) {
    int a, b;
    cin >> a >> b;
    a--;
    b--;
    g[a] |= 1 << b;
    g[b] |= 1 << a;
  }
  for (int i = 0; i < n; i++) g[i] |= 1 << i;

  const int inf = 1 << 10;
  vector<int> dp(1 << n, inf);
  dp[0] = 0;

  for (int s = 1; s < 1 << n; s++) {
    int t = s;
    for (int i = 0; i < n; i++)
      if (s >> i & 1) t &= g[i];
    if (t == s) {
      dp[s] = 1;
      continue;
    }
    for (int t = s; t > 0; --t &= s) {
      dp[s] = min(dp[s], dp[t] + dp[s ^ t]);
    }
  }
  cout << dp[(1 << n) - 1] << endl;
}
