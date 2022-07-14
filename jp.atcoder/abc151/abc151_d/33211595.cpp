#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int h, w;
  cin >> h >> w;
  int const inf = 1 << 29;
  vector<string> maze(h);
  for(int i = 0; i < h; i++) cin >> maze[i];
  auto on_grid = [&](int y, int x) -> bool {
    return 0 <= y && y < h && 0 <= x && x < w;
  };
  int n = h * w;
  vector<vector<int>> g(n, vector<int>(n, inf));
  for(int i = 0; i < h; i++) {
    for(int j = 0; j < w; j++) {
      if(maze[i][j] == '#') continue;
      int u = i * w + j;
      for(int dy = -1; dy < 2; dy++) {
        for(int dx = -1; dx < 2; dx++) {
          if(abs(dy) + abs(dx) != 1) continue;
          int ny = i + dy, nx = j + dx;
          if(!on_grid(ny, nx) || maze[ny][nx] == '#') continue;
          int v = ny * w + nx;
          g[u][v] = 1;
        }
      }
    }
  }
  for(int i = 0; i < n; i++) g[i][i] = 0;
  for(int k = 0; k < n; k++) {
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < n; j++) { g[i][j] = min(g[i][j], g[i][k] + g[k][j]); }
    }
  }
  int mx = 0;
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      if(g[i][j] == inf) continue;
      mx = max(mx, g[i][j]);
    }
  }
  cout << mx << endl;
}
