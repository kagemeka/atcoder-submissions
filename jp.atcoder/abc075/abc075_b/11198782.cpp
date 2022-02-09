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

  vector<vector<int>> res(h+2, vector<int>(w+2));
  for (int i = 1; i <= h; i++) {
    for (int j = 1; j <= w; j++) {
      if (grid[i][j] == '#') {
        for (int dy = -1; dy < 2; dy++) {
          for (int dx = -1; dx < 2; dx++) {
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
