#include <bits/stdc++.h>
using namespace std;
struct fenwick {
  vector<int> data;
  fenwick(int size): data(size + 1) {}
  auto size() -> int { return data.size() - 1; }
  auto add(int i, int x) {
    for(i++; i <= size(); i += i & -i) data[i] += x;
  }
  auto get(int i) -> int {
    int v = 0;
    for(; i > 0; i -= i & -i) { v += data[i]; }
    return v;
  }
};
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<vector<int>> g(n);
  for(int i = 0; i < n - 1; i++) {
    int p;
    cin >> p;
    p--;
    g[p].push_back(i + 1);
    g[i + 1].push_back(p);
  }
  vector<int> tour;
  vector<int> parent(n, -1);
  function<void(int)> euler_tour;
  vector<int> first_idx(n);
  vector<int> last_idx(n);
  vector<int> depth(n, 0);
  euler_tour = [&](int u) -> void {
    first_idx[u] = tour.size();
    tour.push_back(u);
    for(auto& v: g[u]) {
      if(v == parent[u]) continue;
      parent[v] = u;
      depth[v] = depth[u] + 1;
      euler_tour(v);
    }
    last_idx[u] = tour.size();
    tour.push_back(~u);
  };
  euler_tour(0);
  vector<vector<int>> dep_nodes(n);
  for(int i = 0; i < n; i++) dep_nodes[depth[i]].push_back(i);
  int q;
  cin >> q;
  using pi = pair<int, int>;
  vector<vector<pi>> dep_queries(n);
  vector<int> res(q);
  for(int i = 0; i < q; i++) {
    int u, d;
    cin >> u >> d;
    u--;
    dep_queries[d].push_back({i, u});
  }
  fenwick fw(2 * n);
  for(int d = 0; d < n; d++) {
    for(auto& u: dep_nodes[d]) {
      fw.add(0, 1);
      fw.add(first_idx[u] + 1, -1);
    }
    for(auto& [i, u]: dep_queries[d]) {
      res[i] = fw.get(first_idx[u] + 1) - fw.get(last_idx[u] + 1);
    }
    for(auto& u: dep_nodes[d]) {
      fw.add(0, -1);
      fw.add(first_idx[u] + 1, 1);
    }
  }
  for(auto& x: res) cout << x << endl;
}
