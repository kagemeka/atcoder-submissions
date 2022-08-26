#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<vector<int>> a(n, vector<int>(m));
  int sy = 0, sx = 0, gy = 0, gx = 0;
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < m; j++) {
      char x;
      cin >> x;
      if(x == 'S') {
        sy = i;
        sx = j;
        x = '0';
      }
      if(x == 'G') {
        gy = i;
        gx = j;
        x = '0';
      }
      a[i][j] = x - '0';
    }
  }
  int const inf = 1 << 30;
  vector<vector<vector<int>>> dist(
    n, vector<vector<int>>(m, vector<int>(10, inf))
  );
  dist[sy][sx][0] = 0;
  using tup = tuple<int, int, int>;
  queue<tup> que;
  que.emplace(sy, sx, 0);
  vector<pair<int, int>> dyx = {
    {-1,  0},
    { 0, -1},
    { 1,  0},
    { 0,  1}
  };
  auto on_grid = [&](int i, int j) -> bool {
    return 0 <= i && i < n && 0 <= j && j < m;
  };
  while(que.size()) {
    auto [y, x, d] = que.front();
    que.pop();
    for(auto& [dy, dx]: dyx) {
      int ny = y + dy;
      int nx = x + dx;
      if(!on_grid(ny, nx)) continue;
      int nd = d + (a[ny][nx] == d + 1);
      int dv = dist[y][x][d] + 1;
      if(dv >= dist[ny][nx][nd]) continue;
      dist[ny][nx][nd] = dv;
      que.emplace(ny, nx, nd);
    }
  }
  int res = dist[gy][gx][9];
  cout << (res == inf ? -1 : res) << '\n';
}
