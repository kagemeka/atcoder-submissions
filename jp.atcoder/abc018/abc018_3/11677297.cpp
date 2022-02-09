#include <bits/stdc++.h>
using namespace std;
int INF = 1001;

void distance_transform(vector<vector<int>> &grid) {
  int h = grid.size(), w = grid[0].size();
  queue<vector<int>> q;
  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      if (grid[i][j] == 0) {
        q.push({i, j});
      }
    }
  }
  vector<vector<int>> dyx = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
  while (!q.empty()) {
    auto tmp = q.front(); q.pop();
    int y = tmp[0];
    int x = tmp[1];
    for (int k = 0; k < 4; k++) {
      int i = y + dyx[k][0];
      int j = x + dyx[k][1];
      if (i < 0 || i >= h || j < 0 || j >= w) continue;
      if (grid[i][j] <= grid[y][x] + 1) continue;
      grid[i][j] = grid[y][x] + 1;
      q.push({i, j});
    }
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int r, c, k;
  cin >> r >> c >> k;
  vector<vector<int>> grid(r + 2, vector<int>(c + 2));
  for (int i = 1; i < r + 1; i++) {
    for (int j = 1; j < c + 1; j++) {
      char cell;
      cin >> cell;
      grid[i][j] = (cell == 'o') * INF;
    }
  }
  distance_transform(grid);
  int cnt = 0;
  for (int i = 1; i < r + 1; i++) {
    for (int j = 1; j < c + 1; j++) {
      cnt += grid[i][j] >= k;
    }
  }
  cout << cnt << '\n';
  return 0;
}
