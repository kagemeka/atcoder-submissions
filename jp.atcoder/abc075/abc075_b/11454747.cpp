#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int h, w;
  cin >> h >> w;
  vector<vector<char>> grid(h + 2, vector<char>(w + 2, '-'));
  for (int i = 1; i < h + 1; i++) {
    for (int j = 1; j < w + 1; j++) {
      cin >> grid[i][j];
    }
  }
  vector<vector<int>> res(h + 2, vector<int>(w + 2, 0));
  for (int i = 1; i < h + 1; i++) {
    for (int j = 1; j < w + 1; j++) {
      if (grid[i][j] == '.') continue;
      for (int di = -1; di <= 1; di++) {
        for (int dj = -1; dj <= 1; dj++) {
          if (di == 0 && dj == 0) continue;
          res[i+di][j+dj]++;
        }
      }
    }
  }
  for (int i = 1; i < h + 1; i++) {
    for (int j = 1; j < w + 1; j++) {
      if (grid[i][j] == '#') cout << '#';
      else cout << res[i][j];
    }
    cout << '\n';
  }
  return 0;
}
