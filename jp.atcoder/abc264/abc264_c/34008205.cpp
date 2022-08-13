#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int h, w;
  cin >> h >> w;
  vector<vector<int>> a(h, vector<int>(w));
  for(int i = 0; i < h; i++) {
    for(int j = 0; j < w; j++) { cin >> a[i][j]; }
  }
  int h2, w2;
  cin >> h2 >> w2;
  vector<vector<int>> b(h2, vector<int>(w2));
  for(int i = 0; i < h2; i++) {
    for(int j = 0; j < w2; j++) { cin >> b[i][j]; }
  }
  auto popcnt = [&](int i) -> int { return __builtin_popcount(i); };
  auto possible = [&](int s, int t) -> bool {
    int n = h2;
    int m = w2;
    if(popcnt(s) != n || popcnt(t) != m) return false;
    vector<int> ys, xs;
    for(int i = 0; i < h; i++) {
      if(s >> i & 1) ys.push_back(i);
    }
    for(int j = 0; j < w; j++) {
      if(t >> j & 1) xs.push_back(j);
    }
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < m; j++) {
        if(a[ys[i]][xs[j]] != b[i][j]) return false;
      }
    }
    return true;
  };
  for(int s = 0; s < 1 << h; s++) {
    for(int t = 0; t < 1 << w; t++) {
      if(possible(s, t)) {
        cout << "Yes" << endl;
        return 0;
      }
    }
  }
  cout << "No" << endl;
}
