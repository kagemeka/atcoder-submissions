#include <bits/stdc++.h>
using namespace std;

int main() {
  int h, w;
  cin >> h >> w;
  char grid[h+2][w+2];
  for (int i = 1; i <= h; i++) {
    for (int j = 1; j <= w; j++) {
      cin >> grid[i][j];
    }
  }

  int res[h+2][w+2];
  for (int i = 0; i < h+2; i++) {
    for (int j = 0; j < w+2; j++) {
      res[i][j] = 0;
    }
  }

  for (int i = 1; i <= h; i++) {
    for (int j = 1; j <= w; j++) {
      if (grid[i][j] == '#') {
        for (int dy = -1; dy < 2; dy++) {
          for (int dx = -1; dx < 2; dx++) {
            // cout << dy << " " << dx << endl;
            if (dy == 0 && dx == 0) continue;
            res[i+dy][j+dx]++;
          }
        }
      }
    }
  }

  for (int i = 1; i < h+1; i++) {
    for (int j = 1; j < w+1; j++) {
      if (grid[i][j] == '#') {
        cout << '#';
      } else {
        cout << res[i][j];
      }
    }
    cout << endl;
  }

  return 0;
}
