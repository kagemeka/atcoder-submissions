#include <bits/stdc++.h>
using namespace std;
auto solve() -> void {
  long const mod = 1000000007;
  long const inv_2 = (mod + 1) >> 1;
  long n, a, b;
  cin >> n >> a >> b;
  long s = max(0l, n - a - b + 1);
  // s %= mod;
  long s2 = (s + 1) * s % mod * inv_2 % mod;
  long c0 = (n - a + 1) * (n - b + 1) % mod * s2 % mod;
  long c1 = s2 * s2 % mod;
  cout << (4 * (c0 - c1) % mod + mod) % mod << endl;
}
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int t;
  cin >> t;
  while(t--) { solve(); }
}
