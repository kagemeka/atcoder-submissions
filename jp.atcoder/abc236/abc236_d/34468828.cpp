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
  queue<pair<int, int>> que;
  que.emplace(0, 0);
  int mx = 0;
  int full = (1 << n2) - 1;
  while(que.size()) {
    auto [s, v] = que.front();
    que.pop();
    if(s == full) {
      mx = max(mx, v);
      continue;
    }
    int i = __builtin_ctz(~s & -~s);
    int t = s | 1 << i;
    for(int j = i + 1; j < n2; j++) {
      if(s >> j & 1) continue;
      que.emplace(t | 1 << j, v ^ a[i][j]);
    }
  }
  cout << mx << endl;
}
