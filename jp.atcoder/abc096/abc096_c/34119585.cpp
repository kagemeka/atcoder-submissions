#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int h, w;
  cin >> h >> w;
  vector<string> a(h);
  for(int i = 0; i < h; i++) cin >> a[i];
  for(int i = 0; i < h; i++) {
    for(int j = 0; j < w; j++) {
      if(a[i][j] == '.') continue;
      int cnt = 0;
      for(int dy = -1; dy < 2; dy++) {
        for(int dx = -1; dx < 2; dx++) {
          if(abs(dx) + abs(dy) != 1) continue;
          int ny = i + dy;
          int nx = j + dx;
          if(ny < 0 || h <= ny) continue;
          if(nx < 0 || w <= nx) continue;
          cnt += a[ny][nx] == '#';
        }
      }
      if(!cnt) {
        cout << "No" << endl;
        return 0;
      }
    }
  }
  cout << "Yes" << endl;
}
