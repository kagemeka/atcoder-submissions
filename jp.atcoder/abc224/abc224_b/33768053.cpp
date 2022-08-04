#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int h, w;
  cin >> h >> w;
  vector<vector<int>> a(h, vector<int>(w));
  for(int i = 0; i < h; i++) {
    for(int j = 0; j < w; j++) { cin >> a[i][j]; }
  }
  auto f = [&](int i, int j) -> bool {
    for(int y = i + 1; y < h; y++) {
      for(int x = j + 1; x < w; x++) {
        int l = a[i][j] + a[y][x];
        int r = a[i][x] + a[y][j];
        if(l > r) return false;
      }
    }
    return true;
  };
  for(int i = 0; i < h; i++) {
    for(int j = 0; j < w; j++) {
      if(!f(i, j)) {
        cout << "No" << endl;
        return 0;
      }
    }
  }
  cout << "Yes" << endl;
}
