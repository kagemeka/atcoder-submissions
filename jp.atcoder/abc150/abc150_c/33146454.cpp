#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> p(n), q(n);
  for(int i = 0; i < n; i++) cin >> p[i];
  for(int i = 0; i < n; i++) cin >> q[i];
  int d = 0;
  vector<int> fact(n);
  fact[0] = 1;
  for(int i = 0; i < n - 1; i++) fact[i + 1] = (i + 1) * fact[i];
  int sp = 0, sq = 0;
  for(int i = 0; i < n; i++) {
    int cp = __builtin_popcount(sp & ((1 << p[i]) - 1));
    int cq = __builtin_popcount(sq & ((1 << q[i]) - 1));
    d += (p[i] - cp - q[i] + cq) * fact[n - i - 1];
    sp |= 1 << p[i];
    sq |= 1 << q[i];
  }
  cout << abs(d) << endl;
}
