#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  int n2 = n << 1;
  vector<vector<int>> a(n2, vector<int>(n2));
  for(int i = 0; i < n2 - 1; i++) {
    for(int j = i + 1; j < n2; j++) { cin >> a[i][j]; }
  }
  function<int(int, int)> dfs;
  int full = (1 << n2) - 1;
  dfs = [&](int s, int v) -> int {
    if(s == full) { return v; }
    int i = __builtin_ctz(~s & -~s);
    int mx = 0;
    int t = s | 1 << i;
    for(int j = i + 1; j < n2; j++) {
      if(s >> j & 1) continue;
      mx = max(mx, dfs(t | 1 << j, v ^ a[i][j]));
    }
    return mx;
  };
  cout << dfs(0, 0) << endl;
}
