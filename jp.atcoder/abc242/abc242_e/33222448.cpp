#include <bits/stdc++.h>
using namespace std;
auto solve() -> void {
  int n;
  string s;
  cin >> n >> s;
  long const mod = 998244353;
  long dp0 = 1, dp1 = 0;
  int m = (n + 1) >> 1;
  for(int i = 0; i < m; i++) {
    int d = s[i] - 'A';
    dp1 = dp1 * 26l % mod + dp0 * d;
    dp1 %= mod;
  }
  string t0 = s.substr(0, n >> 1), t1 = s.substr(m, n >> 1);
  reverse(t0.begin(), t0.end());
  // cout << t0 << endl;
  // cout << t1 << endl;
  dp0 *= t0 <= t1;
  cout << (dp0 + dp1) % mod << endl;
  ;
}
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int t;
  cin >> t;
  while(t--) { solve(); }
}
