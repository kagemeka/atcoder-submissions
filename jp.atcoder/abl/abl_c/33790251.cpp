#include <bits/stdc++.h>
using namespace std;
struct union_find {
  vector<int> data;
  union_find(int size): data(size, -1) {}
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
  int n, m;
  cin >> n >> m;
  union_find uf(n);
  while(m--) {
    int u, v;
    cin >> u >> v;
    uf.unite(u - 1, v - 1);
  }
  set<int> st;
  for(int i = 0; i < n; i++) st.insert(uf.root(i));
  cout << (int)st.size() - 1 << endl;
}
