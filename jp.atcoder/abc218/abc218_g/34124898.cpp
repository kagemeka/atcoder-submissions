#include <bits/stdc++.h>
using namespace std;
template<typename T> class fenwick {
  vector<T> node;

public:
  fenwick(int size): node(size + 1) {}
  auto size() -> int { return node.size() - 1; }
  auto operate(int i, T x) -> void {
    assert(0 <= i);
    for(i++; i <= size(); i += i & -i) node[i] += x;
  }
  auto get(int i) -> T {
    T v = 0;
    for(; i > 0; i -= i & -i) v += node[i];
    return v;
  }
  template<typename F> auto max_right(F f) -> int {
    int n = size();
    int d = 1 << ((int)log2(n + 1) + 1);
    T v = 0;
    int i = 0;
    while(true) {
      d >>= 1;
      if(!d) return i;
      if(i + d > n) continue;
      auto nv = v + node[i + d];
      if(f(nv)) {
        i += d;
        v = nv;
      }
    }
  }
};
class fw_multiset {
  fenwick<int> fw;

public:
  fw_multiset(int less_than): fw(less_than) {}
  auto size() -> int { return fw.get(fw.size()); }
  auto count(int x) -> int { return fw.get(x + 1) - fw.get(x); }
  auto add(int x, int delta) { fw.operate(x, delta); }
  auto lower_bound(int x) -> int { return fw.get(x); }
  auto upper_bound(int x) -> int { return fw.get(x + 1); }
  auto operator[](int i) -> int {
    return fw.max_right([&](int x) { return x <= i; });
  }
};
template<typename A> auto unique(A a) -> A {
  sort(a.begin(), a.end());
  a.erase(std::unique(a.begin(), a.end()), a.end());
  return a;
}
template<typename T> struct array_compression {
  vector<T> values;
  template<typename A> array_compression(A a) {
    values = unique(vector<T>(a.begin(), a.end()));
  }
  auto size() -> int { return values.size(); }
  auto operator()(T x) -> int {
    int i = lower_bound(values.begin(), values.end(), x) - values.begin();
    assert(i < (int)values.size() && values[i] == x);
    return i;
  }
  auto operator[](int i) const -> T { return values[i]; }
  template<typename A> static auto once(A a) -> std::vector<int> {
    auto f = array_compression(a);
    vector<int> indices(a.size());
    for(int i = 0; i < (int)a.size(); ++i) indices[i] = f(a[i]);
    return indices;
  }
};
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  vector<vector<int>> g(n);
  for(int i = 0; i < n - 1; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  function<int(int, int, int)> dfs;
  array_compression<int> f(a);
  fw_multiset st(1 << 17);
  dfs = [&](int u, int p, int turn) -> int {
    int x = f(a[u]);
    st.add(x, 1);
    vector<int> cand;
    for(auto& v: g[u]) {
      if(v == p) continue;
      cand.push_back(dfs(v, u, turn ^ 1));
    }
    sort(cand.begin(), cand.end());
    if(turn == 0) reverse(cand.begin(), cand.end());
    int res;
    if(cand.size()) res = cand.front();
    else {
      int m = st.size();
      res = (f[st[m >> 1]] + f[st[(m - 1) >> 1]]) >> 1;
    }
    st.add(x, -1);
    return res;
  };
  cout << dfs(0, -1, 0) << endl;
}
