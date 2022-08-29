#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int h, w, d;
  cin >> h >> w >> d;
  vector<pair<int, int>> idx(h * w);
  for(int i = 0; i < h; i++) {
    for(int j = 0; j < w; j++) {
      int x;
      cin >> x;
      x--;
      idx[x] = {i, j};
    }
  }
  vector<int> s(h * w);
  for(int i = 0; i < h * w - d; i++) {
    auto [x, y] = idx[i];
    auto [a, b] = idx[i + d];
    s[i + d] = s[i] + abs(x - a) + abs(y - b);
  }
  int q;
  cin >> q;
  while(q--) {
    int l, r;
    cin >> l >> r;
    l--;
    r--;
    cout << s[r] - s[l] << '\n';
  }
}
