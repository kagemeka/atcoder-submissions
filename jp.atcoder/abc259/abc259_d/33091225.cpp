#include <bits/stdc++.h>
using namespace std;
template<typename G> auto connected_components(const G& g) -> vector<int> {
  int n = g.size();
  queue<int> que;
  vector<int> ids(n, -1);
  int id = 0;
  for(int i = 0; i < n; i++) {
    if(ids[i] != -1) continue;
    ids[i] = id;
    que.push(i);
    while(!que.empty()) {
      int u = que.front();
      que.pop();
      for(auto& v: g[u]) {
        if(ids[v] != -1) continue;
        ids[v] = id;
        que.push(v);
      }
    }
    id++;
  }
  return ids;
}
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  // find s, t  circle
  long sx, sy, tx, ty;
  cin >> sx >> sy >> tx >> ty;
  using tup = tuple<long, long, long>;
  vector<tup> circles(n);
  auto dist2 = [&](long x0, long y0, long x1, long y1) {
    return (x0 - x1) * (x0 - x1) + (y0 - y1) * (y0 - y1);
  };
  int sid = 0, tid = 0;
  for(int i = 0; i < n; i++) {
    long x, y, r;
    cin >> x >> y >> r;
    circles[i] = {x, y, r};
    if(dist2(x, y, sx, sy) == r * r) { sid = i; }
    if(dist2(x, y, tx, ty) == r * r) { tid = i; }
  }
  vector<vector<int>> g(n);
  for(int i = 0; i < n; i++) {
    auto [xi, yi, ri] = circles[i];
    for(int j = 0; j < i; j++) {
      auto [xj, yj, rj] = circles[j];
      auto d = dist2(xi, yi, xj, yj);
      if(d <= (ri + rj) * (ri + rj) && d >= (ri - rj) * (ri - rj)) {
        g[i].push_back(j);
        g[j].push_back(i);
      }
    }
  }
  auto ids = connected_components(g);
  cout << (ids[sid] == ids[tid] ? "Yes" : "No") << endl;
}
