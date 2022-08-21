#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  // shakutor
  int n;
  long p, q, r;
  cin >> n >> p >> q >> r;
  vector<long> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int x = 0, y = 0, z = 0, w = 0;
  // long sum = 0;
  long s0 = 0, s1 = 0, s2 = 0;
  while(x <= n - 3) {
    while(s0 < p && y < n - 2) {
      s1 -= a[y];
      s0 += a[y];
      y++;
    }
    if(s0 != p) {}
    while(s1 < q && z < n - 1) {
      s2 -= a[z];
      s1 += a[z];
      z++;
    }
    while(s2 < r && w < n) {
      s2 += a[w];
      w++;
    }
    if(s0 == p && s1 == q && s2 == r) {
      cout << "Yes" << endl;
      return 0;
    }
    s0 -= a[x];
    x++;
  }
  cout << "No" << endl;
}
