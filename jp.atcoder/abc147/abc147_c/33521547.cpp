#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> g(n, (1 << n) - 1);
  for(int i = 0; i < n; i++) {
    int m;
    cin >> m;
    while(m--) {
      int x, y;
      cin >> x >> y;
      if(y) continue;
      x--;
      g[i] &= ~(1 << x);
    }
  }
  int mx = 0;
  for(int s = 0; s < 1 << n; s++) {
    int cnt = 0;
    int t = (1 << n) - 1;
    for(int i = 0; i < n; i++) {
      if(~s >> i & 1) continue;
      t &= g[i];
      cnt++;
    }
    if(t == s) { mx = max(mx, cnt); }
  }
  cout << mx << endl;
}
