#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int r, c, sy, sx, gy, gx;
  cin >> r >> c >> sy >> sx >> gy >> gx;
  sy--; sx--; gy--; gx--;
  vector<vector<char>> maze(r, vector<char>(c));
  for (int i = 0; i < r; i++) {
    for (int j = 0; j < c; j++) {
      cin >> maze[i][j];
    }
  }
  vector<vector<bool>> visited(r, vector<bool>(c));
  queue<tuple<int, int, int>> q;
  q.push(make_tuple(sy, sx, 0));
  vector<tuple<int, int>> dd;
  for (int i = -1; i < 2; i++) {
    for (int j = -1; j < 2; j++) {
      if (abs(abs(i) - abs(j)) == 1) {
        dd.push_back(make_tuple(i, j));
      }
    }
  }
  while (!q.empty()) {
    tuple<int, int, int> nex = q.front();
    q.pop();
    int y, x, d;
    y = get<0>(nex);
    x = get<1>(nex);
    d = get<2>(nex);
    if (visited[y][x]) continue;
    visited[y][x] = true;
    if (y == gy && x == gx) {
      cout << d << '\n';
      return 0;
    }
    for (auto &dyx : dd) {
      int &dy = get<0>(dyx);
      int &dx = get<1>(dyx);
      int i = y + dy;
      int j = x + dx;
      if ((!visited[i][j]) && maze[i][j] == '.') {
        q.push(make_tuple(i, j, d+1));
      }
    }
  }
}
