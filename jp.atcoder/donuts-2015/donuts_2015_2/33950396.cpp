#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  vector<int> b(m), t(m);
  for(int i = 0; i < m; i++) {
    cin >> b[i];
    int k;
    cin >> k;
    for(int j = 0; j < k; j++) {
      int x;
      cin >> x;
      x--;
      t[i] |= 1 << x;
    }
  }
  int mx = 0;
  for(int s = 0; s < 1 << n; s++) {
    if(__builtin_popcount(s) != 9) continue;
    int tot = 0;
    for(int i = 0; i < n; i++)
      if(s >> i & 1) tot += a[i];
    for(int i = 0; i < m; i++) {
      if(__builtin_popcount(s & t[i]) >= 3) tot += b[i];
    }
    mx = max(mx, tot);
  }
  cout << mx << endl;
}
