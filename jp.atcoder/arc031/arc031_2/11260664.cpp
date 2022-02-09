#include <bits/stdc++.h>
using namespace std;

bool dfs(vector<vector<char>> &grid, int sy, int sx, vector<vector<int>> &d) {
  int h = grid.size() - 2;
  int w = grid[0].size() - 2;

  vector<vector<bool>> will_visit(h+2, vector<bool>(w+2, false));
  will_visit[sy][sx] = true;

  vector<vector<int>> stack = {{sy, sx}};

  while (!stack.empty()) {
    vector<int> yx(2);
    yx = stack.back();
    stack.pop_back();
    int y = yx[0];
    int x = yx[1];
    for (vector<int> &dyx: d) {
      int i = y + dyx[0];
      int j = x + dyx[1];
      if (will_visit[i][j]) {
        continue;
      }
      if (grid[i][j] == 'o') {
        stack.push_back({i, j});
        will_visit[i][j] = true;
      }
    }
  }
  for (int i = 1; i < h + 1; i++) {
    for (int j = 1; j < w + 1; j++) {
      if (grid[i][j] == 'o') {
        if (!will_visit[i][j]) {
          return false;
        }
      }
    }
  }
  return true;
}

int main() {
  int h, w;
  h = 10;
  w = 10;
  vector<vector<char>> grid(h+2, vector<char>(w+2, 'x'));
  for (int i = 1; i < h+1; i++) {
    for (int j = 1; j < w+1; j++) {
      cin >> grid[i][j];
    }
  }

  vector<vector<int>> d = {
    {-1, 0},
    {0, -1},
    {1, 0},
    {0, 1},
  };

  for (int i = 1; i < h + 1; i++) {
    for (int j = 1; j < w + 1; j++) {
      if (dfs(grid, i, j, d)) {
        cout << "YES" << endl;
        return 0;
      }
    }
  }
  cout << "NO" << endl;
  return 0;
}
