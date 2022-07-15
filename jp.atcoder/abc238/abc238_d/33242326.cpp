#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int t;
  cin >> t;
  while(t--) {
    long a, s;
    cin >> a >> s;
    long x = s - 2 * a;
    bool ok = 0 <= x && x <= s;
    for(int i = 0; i < 60; i++) { ok &= !((a >> i & 1) && (x >> i & 1)); }
    cout << (ok ? "Yes" : "No") << endl;
  }
}
