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

  vector<vector<int>> d = {
    {-1, 0},
    {0, -1},
    {1, 0},
    {0, 1}
  };
  vector<vector<bool>> will_visit(h+2, vector<bool>(w+2, false));
  will_visit[sy][sx] = true;
  vector<vector<int>> stack = {{sy, sx}};
  while (!stack.empty()) {
    int y, x;
    vector<int> yx(2);
    yx = stack.back();
    stack.pop_back();
    y = yx[0];
    x = yx[1];
    for (vector<int> &dyx: d) {
      int &dy = dyx[0];
      int &dx = dyx[1];
      int i, j;
      i = y + dy;
      j = x + dx;
      if (grid[i][j] == '.') {
        if (!will_visit[i][j]) {
          vector<int> ij = {i, j};
          stack.push_back(ij);
          will_visit[i][j] = true;
        }
      }
    }
  }
  string ans = will_visit[gy][gx] ? "Yes" : "No";
  cout << ans << endl;
  return 0;
}
