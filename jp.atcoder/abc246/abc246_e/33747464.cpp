#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  int sy, sx, gy, gx;
  cin >> sy >> sx >> gy >> gx;
  sy--;
  sx--;
  gy--;
  gx--;
  vector<string> grid(n);
  for(int i = 0; i < n; i++) cin >> grid[i];
  auto on_grid = [&](int y, int x) -> bool {
    return 0 <= y && y < n && 0 <= x && x < n;
  };
  vector<pair<int, int>> dyx = {
    {-1, -1},
    {-1,  1},
    { 1, -1},
    { 1,  1}
  };
  // 3 - i -> reverse
  deque<tuple<int, int, int>> que;
  que.emplace_back(sy, sx, 4);
  int const inf = 1 << 29;
  vector<vector<vector<int>>> dist(
    n, vector<vector<int>>(n, vector<int>(5, inf))
  );
  dist[sy][sx][4] = 0;
  while(que.size()) {
    auto [y, x, i] = que.front();
    que.pop_front();
    for(int j = 0; j < 4; j++) {
      int w = 1;
      if(j == i) w = 0;
      auto& [dy, dx] = dyx[j];
      int ny = y + dy, nx = x + dx;
      if(!on_grid(ny, nx) || grid[ny][nx] == '#') continue;
      int dv = dist[y][x][i] + w;
      if(dv >= dist[ny][nx][j]) continue;
      dist[ny][nx][j] = dv;
      if(w == 0) que.emplace_front(ny, nx, j);
      else que.emplace_back(ny, nx, j);
    }
  }
  int mn = inf;
  for(int i = 0; i < 4; i++) { mn = min(mn, dist[gy][gx][i]); }
  cout << (mn == inf ? -1 : mn) << endl;
}
