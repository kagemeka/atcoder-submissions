#include <bits/stdc++.h>
using namespace std;

int main() {
  int h, w;
  cin >> h >> w;

  int sy, sx, gy, gx;
  vector<vector<char>> grid(h+2, vector<char>(w+2, '#'));
  for (int i = 1; i < h+1; i++) {
    for (int j = 1; j < w+1; j++) {
      cin >> grid[i][j];
      if (grid[i][j] == 's') {
        sy = i;
        sx = j;
        grid[i][j] = '.';
      } else if (grid[i][j] == 'g') {
        gy = i;
        gx = j;
        grid[i][j] = '.';
      }
    }
  }

  vector<vector<bool>> visited(h+2, vector<bool>(w+2, false));
  vector<vector<int>> stack = {{sy, sx}};
  while (!stack.empty()) {
    int y, x;
    vector<int> yx(2);
    yx = stack.back();
    stack.pop_back();
    y = yx[0];
    x = yx[1];
    visited[y][x] = true;
    for (int dy = -1; dy < 2; dy++) {
      for (int dx = -1; dx < 2; dx++) {
        if (dy == 0 && dx == 0) {
          continue;
        }
        int i, j;
        i = y + dy;
        j = x + dx;
        if (grid[i][j] == '.') {
          if (!visited[i][j]) {
            vector<int> ij = {i, j};
            stack.push_back(ij);
          }
        }
      }
    }
  }
  string ans = visited[gy][gx] ? "Yes" : "No";
  cout << ans << endl;
  return 0;
}
