#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<vector<int>> g(n, vector<int>(2));
  for(int i = 0; i < n; i++) {
    int m;
    cin >> m;
    while(m--) {
      int x, y;
      cin >> x >> y;
      x--;
      g[i][y] |= 1 << x;
    }
  }
  int mx = 0;
  for(int s = 0; s < 1 << n; s++) {
    int cnt = 0;
    bool ok = true;
    for(int i = 0; i < n; i++) {
      if(~s >> i & 1) continue;
      ok = ok && (s | g[i][1]) == s && (~s | g[i][0]) == ~s;
      cnt++;
    }
    if(ok) { mx = max(mx, cnt); }
  }
  cout << mx << endl;
}
