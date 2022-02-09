#include <iostream>
#include <vector>
#include <string>
#include <queue>
using namespace std;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int h, w, sy, sx, gy, gx;
  cin >> h >> w >> sy >> sx >> gy >> gx;
  --sy; --sx; --gy; --gx;
  vector<string> maze(h);
  for (int i = 0; i < h; i++) cin >> maze[i];
  vector<int> dy = {-1, 0, 1, 0};
  vector<int> dx = {0, -1, 0, 1};
  int inf = 1 << 30;
  vector<vector<int>> dist(h, vector<int>(w, inf));
  dist[sy][sx] = 0;
  queue<pair<int, int>> que;
  que.emplace(sy, sx);

  auto on_grid = [&h, &w](const int &y, const int &x) -> bool {
    return 0 <= y && y < h && 0 <= x && x < w;
  };

  while (!que.empty()) {
    auto y = que.front().first, x = que.front().second;
    que.pop();
    for (int i = 0; i < 4; i++) {
      auto ny = y + dy[i], nx = x + dx[i];
      if (!on_grid(ny, nx)) continue;
      if (maze[ny][nx] == '#') continue;
      if (dist[ny][nx] != inf) continue;
      dist[ny][nx] = dist[y][x] + 1;
      que.emplace(ny, nx);
    }
  }
  cout << dist[gy][gx] << '\n';
}
