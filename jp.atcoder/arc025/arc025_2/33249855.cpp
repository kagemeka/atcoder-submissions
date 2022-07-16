#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int h, w;
  cin >> h >> w;
  vector<vector<int>> a(h + 1, vector<int>(w + 1));
  for(int i = 0; i < h; i++) {
    for(int j = 0; j < w; j++) {
      cin >> a[i + 1][j + 1];
      if((i + j) & 1) a[i + 1][j + 1] *= -1;
    }
  }
  for(int i = 0; i < h + 1; i++) {
    for(int j = 0; j < w; j++) a[i][j + 1] += a[i][j];
  }
  for(int i = 0; i < h; i++) {
    for(int j = 0; j < w + 1; j++) a[i + 1][j] += a[i][j];
  }
  int mx = 0;
  for(int dy = 1; dy < h + 1; dy++) {
    for(int dx = 1; dx < w + 1; dx++) {
      for(int i = 0; i < h - dy + 1; i++) {
        for(int j = 0; j < w - dx + 1; j++) {
          int s = a[i + dy][j + dx] - a[i + dy][j] - a[i][j + dx] + a[i][j];
          if(s == 0) mx = max(mx, dy * dx);
        }
      }
    }
  }
  cout << mx << endl;
}
