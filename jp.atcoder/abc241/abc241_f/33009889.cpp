#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int h, w, n;
  cin >> h >> w >> n;

  vector<vector<int>> x_list(h + 1), y_list(w + 1);
  int sx, sy, gx, gy;
  cin >> sy >> sx >> gy >> gx;

  for(int i = 0; i < n; i++) {
    int x, y;
    cin >> y >> x;

    x_list[y].push_back(x);
    y_list[x].push_back(y);
  }
  for(int i = 1; i < h + 1; i++) sort(x_list[i].begin(), x_list[i].end());
  for(int i = 1; i < w + 1; i++) sort(y_list[i].begin(), y_list[i].end());

  long const inf = 1l << 60;
  vector<vector<long>> dist(h + 1, vector<long>(w + 1, inf));
  using pi = pair<int, int>;
  queue<pi> que;
  que.emplace(sy, sx);
  dist[sy][sx] = 0;

  while(que.size()) {
    auto [y, x] = que.front();
    que.pop();
    long nd = dist[y][x] + 1;
    {
      int i = upper_bound(y_list[x].begin(), y_list[x].end(), y) -
              y_list[x].begin() - 1;
      if(i >= 0) {
        int ny = y_list[x][i] + 1;
        if(dist[ny][x] == inf) {
          dist[ny][x] = nd;
          que.emplace(ny, x);
        }
      }
    }
    {
      int i =
        lower_bound(y_list[x].begin(), y_list[x].end(), y) - y_list[x].begin();
      if(i < (int)y_list[x].size()) {
        int ny = y_list[x][i] - 1;
        if(dist[ny][x] == inf) {
          dist[ny][x] = nd;
          que.emplace(ny, x);
        }
      }
    }
    {
      int i = upper_bound(x_list[y].begin(), x_list[y].end(), x) -
              x_list[y].begin() - 1;
      if(i >= 0) {
        int nx = x_list[y][i] + 1;
        if(dist[y][nx] == inf) {
          dist[y][nx] = nd;
          que.emplace(y, nx);
        }
      }
    }
    {
      int i =
        lower_bound(x_list[y].begin(), x_list[y].end(), x) - x_list[y].begin();
      if(i < (int)x_list[y].size()) {
        int nx = x_list[y][i] - 1;
        if(dist[y][nx] == inf) {
          dist[y][nx] = nd;
          que.emplace(y, nx);
        }
      }
    }
  }
  cout << (dist[gy][gx] == inf ? -1 : dist[gy][gx]) << endl;
}