#include <bits/stdc++.h>
using namespace std;
long long INF = numeric_limits<long long>::max();

int heuristic_cost(int &y, int &x, int &gy, int &gx) {
  return abs(gy - y) + abs(gx - x);
}

long long a_star(vector<vector<char>> &maze, int &cost, int &sy, int &sx, int &gy, int &gx) {
  int h = maze.size(), w = maze[0].size();
  vector<vector<long long>> dist(h, vector<long long>(w, INF));
  priority_queue<vector<long long>, vector<vector<long long>>, greater<vector<long long>>> q;
  q.push({heuristic_cost(sy, sx, gy, gx), 0, sy, sx});
  vector<vector<int>> dyx = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
  while (!q.empty()) {
    auto tmp = q.top(); q.pop();
    long long d = tmp[1];
    int y = tmp[2];
    int x = tmp[3];
    if (dist[y][x] != INF) continue;
    dist[y][x] = d;
    if (y == gy && x == gx) return d;
    for (int k = 0; k < 4; k++) {
      int i = y + dyx[k][0];
      int j = x + dyx[k][1];
      if (maze[i][j] == '-') continue;
      if (dist[i][j] != INF) continue;
      int dd = (maze[i][j] == '.') ? 1 : cost;
      long long score = heuristic_cost(i, j, gy, gx) + d + dd;
      q.push({score, d + dd, i, j});
    }
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int sy, sx, gy, gx;
  int h, w, t;
  cin >> h >> w >> t;
  vector<vector<char>> maze(h + 2, vector<char>(w + 2, '-'));
  for (int i = 1; i < h + 1; i++) {
    for (int j = 1; j < w + 1; j++) {
      char c;
      cin >> c;
      if (c == 'S') {
        sy = i;
        sx = j;
        maze[i][j] = '.';
      } else if (c == 'G') {
        gy = i;
        gx = j;
        maze[i][j] = '.';
      } else {
        maze[i][j] = c;
      }
    }
  }
  int lo = 0, hi = t;
  while (lo + 1 < hi) {
    int x = (lo + hi) / 2;
    (a_star(maze, x, sy, sx, gy, gx) <= t) ? lo = x : hi = x;
  }
  cout << lo << '\n';
  return 0;
}
