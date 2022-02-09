#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int h, w; cin >> h >> w;
  vector<vector<char>> grid(h + 2, vector<char>(w + 2));
  for (int i = 1; i < h + 1; i++) {
    for (int j = 1; j < w + 1; j++) {
      cin >> grid[i][j];
    }
  }

  vector<vector<int>> dyx = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
  for (int i = 1; i < h + 1; i++) {
    for (int j = 1; j < w + 1; j++) {
      if (grid[i][j] == '#') {
        bool flag = false;
        for (auto &d : dyx) {
          auto y = i + d[0];
          auto x = j + d[1];
          if (grid[y][x] == '#') {
            flag = true;
            break;
          }
        }
        if (!flag) {
          cout << "No" << '\n';
          return 0;
        }
      }
    }
  }
  cout << "Yes" << '\n';
  return 0;
}
