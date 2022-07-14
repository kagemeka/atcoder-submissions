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
  vector<vector<int>> g(n);
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
          g[u].push_back(v);
        }
      }
    }
  }
  int mx = 0;
  queue<int> que;
  for(int src = 0; src < n; src++) {
    que.push(src);
    vector<int> dist(n, inf);
    dist[src] = 0;
    while(que.size()) {
      int u = que.front();
      que.pop();
      for(auto& v: g[u]) {
        int dv = dist[u] + 1;
        if(dv >= dist[v]) continue;
        dist[v] = dv;
        que.push(v);
      }
    }
    for(int i = 0; i < n; i++) {
      if(dist[i] == inf) continue;
      mx = max(mx, dist[i]);
    }
  }
  cout << mx << endl;
}
