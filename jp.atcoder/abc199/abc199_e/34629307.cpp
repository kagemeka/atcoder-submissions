#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<int> x(m), y(m), z(m);
  for(int i = 0; i < m; i++) {
    cin >> x[i] >> y[i] >> z[i];
    y[i]--;
  }
  int n2 = 1 << n;
  vector<bool> ok(n2, true);
  for(int s = 0; s < n2; s++) {
    vector<int> c(n);
    for(int i = 0; i < n; i++) { c[i] = s >> i & 1; }
    for(int i = 0; i < n - 1; i++) { c[i + 1] += c[i]; }
    for(int i = 0; i < m; i++) {
      if(x[i] < c[n - 1]) continue;
      ok[s] = ok[s] && c[y[i]] <= z[i];
    }
  }
  vector<long> dp(n2);
  dp[0] = 1;
  for(int s = 0; s < n2; s++) {
    for(int i = 0; i < n; i++) {
      if(s >> i & 1) continue;
      int t = s | 1 << i;
      dp[t] += dp[s];
      dp[t] *= ok[t];
    }
  }
  cout << dp[n2 - 1] << endl;
}
