#include <bits/stdc++.h>
using namespace std;
struct union_find {
  vector<int> data;
  union_find(int size): data(size, -1) {}
  auto size() -> int { return data.size(); }
  auto root(int u) -> int { return data[u] < 0 ? u : data[u] = root(data[u]); }
  auto unite(int u, int v) {
    u = root(u), v = root(v);
    if(u == v) return;
    if(data[u] > data[v]) swap(u, v);
    data[u] += data[v];
    data[v] = u;
  }
};
auto main() -> int {
  int n;
  cin >> n;
  vector<vector<double>> dist(n + 2, vector<double>(n + 2));
  vector<double> x(n), y(n);
  for(int i = 0; i < n; i++) cin >> x[i] >> y[i];
  auto calc_dist = [&](int i, int j) -> double {
    if(i > j) swap(i, j);
    double dx, dy;
    if(j < n) {
      dx = x[i] - x[j], dy = y[i] - y[j];
    } else {
      dx = 0;
      dy = j == n ? y[i] + 100 : 100 - y[i];
    }
    return sqrt(dx * dx + dy * dy);
  };
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n + 2; j++) {
      auto d = calc_dist(i, j);
      dist[i][j] = dist[j][i] = d;
    }
  }
  // for (int i = 0; i < n + 2; i++) {
  //   for (int j = 0; j < n + 2; j++) {
  //     cout << dist[i][j] <<" \n"[j == n + 1];
  //   }
  // }
  auto reachable = [&](double r) -> bool {
    double d = r * 2;
    union_find uf(n + 2);
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < n + 2; j++) {
        if(dist[i][j] <= d) uf.unite(i, j);
      }
    }
    return uf.root(n) != uf.root(n + 1);
  };
  double ok = 0, ng = 100;
  for(int t = 0; t < 100; t++) {
    double r = (ok + ng) / 2;
    if(reachable(r)) ok = r;
    else ng = r;
  }
  cout << setprecision(16) << ok << endl;
}
