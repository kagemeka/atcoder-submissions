#include <bits/stdc++.h>
using namespace std;

long long INF = numeric_limits<long long>::max();
typedef pair<int, int> p;
typedef tuple<int, int, int, p> t;
typedef pair<vector<vector<long long>>, vector<vector<p>>> pp;

pp dijkstra(vector<vector<bool>> &passable, int &sy, int &sx) {
  int h = passable.size(), w = passable[0].size();
  vector<vector<long long>> dist(h, vector<long long>(w, INF));
  vector<vector<p>> parent(h, vector<p>(w, p(-1, -1)));
  priority_queue<t, vector<t>, greater<t>> q;
  q.push(t(0, sy, sx, p(-1, -1)));
  vector<p> dyx = {p(-1, 0), p(0, -1), p(1, 0), p(0, 1)};
  // vector<p> dyx; for (int i = -1; i < 2; i++) for (int j = -1; j < 2; j++) if (!(i == 0 && j == 0)) dyx.push_back(p(i, j));
  while (!q.empty()) {
    auto tmp = q.top(); q.pop();
    auto d = get<0>(tmp);
    auto y = get<1>(tmp);
    auto x = get<2>(tmp);
    auto par = get<3>(tmp);
    if (dist[y][x] != INF) continue;
    dist[y][x] = d;
    parent[y][x] = par;
    for (auto &nxt : dyx) {
      int i = y + get<0>(nxt);
      int j = x + get<1>(nxt);
      if (!passable[i][j] || dist[i][j] != INF) continue;
      q.push(t(d + 1, i, j, p(y, x)));
    }
  }
  return pp(dist, parent);
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
  auto res = dijkstra(passable, sy, sx);
  auto dist = res.first;
  cout << dist[gy][gx] << '\n';
  return 0;
}
