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
  auto size_of(int u) -> int { return -data[root(u)]; }
};
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, k;
  cin >> n >> k;
  vector<int> a(n);
  for(int i = 0; i < n; i++) {
    int x;
    cin >> x;
    x--;
    a[i] = x;
  }
  union_find uf(n);
  // priority_queue<int, vector<int>, greater<>> que;
  set<int> st;
  vector<vector<int>> cards(n);
  vector<int> res(n, -1);
  vector<int> root(n);
  for(int i = 0; i < n; i++) root[i] = i;
  for(int i = 0; i < n; i++) {
    int x = a[i];
    auto ptr = st.lower_bound(x);
    if(ptr == st.end()) {
      if(k == 1) {
        res[x] = i + 1;
      } else {
        st.insert(x);
        cards[x].push_back(x);
      }
      continue;
    }
    int y = *ptr;
    st.erase(y);
    uf.unite(x, y);
    root[x] = root[y];
    int r = root[x];
    cards[r].push_back(x);
    if(uf.size_of(x) >= k) {
      for(auto& y: cards[r]) { res[y] = i + 1; }
    } else {
      st.insert(x);
    }
  }
  for(auto& x: res) cout << x << endl;
}
