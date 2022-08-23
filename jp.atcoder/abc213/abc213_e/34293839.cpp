#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int h, w;
  cin >> h >> w;
  vector<string> s(h);
  for(int i = 0; i < h; i++) cin >> s[i];
  deque<pair<int, int>> que;
  que.emplace_front(0, 0);
  auto on_grid = [&](int i, int j) -> bool {
    return 0 <= i && i < h && 0 <= j && j < w;
  };
  int const inf = 1 << 30;
  vector<vector<int>> dist(h, vector<int>(w, inf));
  dist[0][0] = 0;
  while(que.size()) {
    auto [y, x] = que.front();
    que.pop_front();
    int du = dist[y][x];
    for(int dy = -2; dy < 3; dy++) {
      for(int dx = -1; dx < 3; dx++) {
        if(abs(dy) + abs(dx) > 3) continue;
        int ny = y + dy;
        int nx = x + dx;
        if(!on_grid(ny, nx)) continue;
        if(abs(dy) + abs(dx) == 1 && s[ny][nx] == '.') {
          int dv = du;
          if(dv >= dist[ny][nx]) continue;
          dist[ny][nx] = dv;
          que.emplace_front(ny, nx);
        }
        int dv = du + 1;
        if(dv >= dist[ny][nx]) continue;
        dist[ny][nx] = dv;
        que.emplace_back(ny, nx);
      }
    }
  }
  cout << dist[h - 1][w - 1] << endl;
}
