#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int h, w, n;
  cin >> h >> w >> n;

  vector<int> y(n + 2), x(n + 2);
  set<int> y_all, x_all;
  for(int i = 0; i < n + 2; i++) {
    cin >> y[i] >> x[i];
    for(int j = -1; j < 2; j++) {
      y_all.insert(y[i] + j);
      x_all.insert(x[i] + j);
    }
  }
  h = y_all.size();
  w = x_all.size();
  vector<vector<int>> x_list(h + 1), y_list(w + 1);

  for(int i = 0; i < n + 2; i++) {
    y[i] = *y_all.lower_bound(y[i]);
    x[i] = *x_all.lower_bound(x[i]);
    // y[i] = distance(y_all.begin(), y_all.find(y[i]));
    // x[i] = distance(x_all.begin(), x_all.find(x[i]));
    if(i >= 2) {
      x_list[y[i]].push_back(x[i]);
      y_list[x[i]].push_back(y[i]);
    }
  }
  for(int i = 1; i < h + 1; i++) sort(x_list[i].begin(), x_list[i].end());
  for(int i = 1; i < w + 1; i++) sort(y_list[i].begin(), y_list[i].end());

  // long const inf = 1l << 60;

  using pi = pair<int, int>;
  map<pi, long> dist;
  queue<pi> que;
  que.emplace(y[0], x[0]);
  dist[{y[0], x[0]}] = 0;

  while(que.size()) {
    auto [y, x] = que.front();
    que.pop();
    long nd = dist[{y, x}] + 1;
    {
      int i = upper_bound(y_list[x].begin(), y_list[x].end(), y) -
              y_list[x].begin() - 1;
      if(i >= 0) {
        int ny = y_list[x][i] + 1;
        if(!dist.count({ny, x})) {
          dist[{ny, x}] = nd;
          que.emplace(ny, x);
        }
      }
    }
    {
      int i =
        lower_bound(y_list[x].begin(), y_list[x].end(), y) - y_list[x].begin();
      if(i < (int)y_list[x].size()) {
        int ny = y_list[x][i] - 1;
        if(!dist.count({ny, x})) {
          dist[{ny, x}] = nd;
          que.emplace(ny, x);
        }
      }
    }
    {
      int i = upper_bound(x_list[y].begin(), x_list[y].end(), x) -
              x_list[y].begin() - 1;
      if(i >= 0) {
        int nx = x_list[y][i] + 1;
        if(!dist.count({y, nx})) {
          dist[{y, nx}] = nd;
          que.emplace(y, nx);
        }
      }
    }
    {
      int i =
        lower_bound(x_list[y].begin(), x_list[y].end(), x) - x_list[y].begin();
      if(i < (int)x_list[y].size()) {
        int nx = x_list[y][i] - 1;
        if(!dist.count({y, nx})) {
          dist[{y, nx}] = nd;
          que.emplace(y, nx);
        }
      }
    }
  }
  cout << (!dist.count({y[1], x[1]}) ? -1 : dist[{y[1], x[1]}]) << endl;
}