#include <bits/stdc++.h>
using namespace std;

long long INF = numeric_limits<long long>::max();
typedef pair<int, int> p;
typedef tuple<double, int, int, int, p> t;
typedef pair<int, vector<vector<p>>> pivvp;

double heuristic_cost(int y, int x, int gy, int gx) {
  return abs(gy - y) + abs(gx - x);
  // return sqrt(pow(gy - y, 2 + pow(gx - x, 2)));
}

pivvp a_star(vector<vector<bool>> &passable, int &sy, int &sx, int &gy, int &gx) {
  int h = passable.size(), w = passable[0].size();
  vector<vector<long long>> dist(h, vector<long long>(w, INF));
  vector<vector<p>> parent(h, vector<p>(w, p(-1, -1)));
  priority_queue<t, vector<t>, greater<t>> q;
  q.push(t(heuristic_cost(sy, sx, gy, gx), 0, sy, sx, p(-1, -1)));
  vector<p> dyx = {p(-1, 0), p(0, -1), p(1, 0), p(0, 1)};
  // vector<p> dyx; for (int i = -1; i < 2; i++) for (int j = -1; j < 2; j++) if (!(i == 0 && j == 0)) dyx.push_back(p(i, j));
  while (!q.empty()) {
    auto tmp = q.top(); q.pop();
    int c, d, y, x; p par;
    c = get<0>(tmp);
    d = get<1>(tmp);
    y = get<2>(tmp);
    x = get<3>(tmp);
    par = get<4>(tmp);
    if (dist[y][x] != INF) continue;
    dist[y][x] = d;
    parent[y][x] = par;
    if (y == gy && x == gx) break;
    for (auto &nxt : dyx) {
      int i = y + get<0>(nxt);
      int j = x + get<1>(nxt);
      if (!passable[i][j] || dist[i][j] != INF) continue;
      int score = heuristic_cost(i, j, gy, gx) + d + 1;
      q.push(t(score, d + 1, i, j, p(y, x)));
    }
  }
  return pivvp(dist[gy][gx], parent);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int r, c, sy, sx, gy, gx;
  cin >> r >> c >> sy >> sx >> gy >> gx;
  sy--; sx--; gy--; gx--;
  vector<vector<bool>> passable(r, vector<bool>(c));
  for (int i = 0; i < r; i++) {
    for (int j = 0; j < c; j++) {
      char o;
      cin >> o;
      passable[i][j] = o == '.';
    }
  }
  auto res = a_star(passable, sy, sx, gy, gx);
  int ans = res.first;
  cout << ans << '\n';
  return 0;
}
