#include <bits/stdc++.h>
using namespace std;
auto bit_length(int n) -> int { return 32 - __builtin_clz(n); }
template<typename G> class segtree {
  using T = typename G::T;
  vector<T> data;
  G g;
  auto merge(int i) { data[i] = g.op(data[i << 1], data[i << 1 | 1]); }
  [[nodiscard]] auto n() const -> int { return data.size() >> 1; }

public:
  int size;
  segtree(G g, int size): g(g), size(size) {
    assert(size > 0);
    int n = 1 << bit_length(size - 1);
    data.resize(n << 1, g.e());
  }
  auto set(int i, T x) {
    assert(0 <= i && i < size);
    for(data[i += n()] = x, i >>= 1; i >= 1; i >>= 1) merge(i);
  }
  auto operator[](int i) -> T { return data[i + n()]; }
  auto operator[](pair<int, int> lr) const -> T {
    auto [l, r] = lr;
    assert(0 <= l && l <= r && r <= size);
    T vl = g.e(), vr = g.e();
    l += n();
    r += n();
    while(l < r) {
      if(l & 1) vl = g.op(vl, data[l++]);
      if(r & 1) vr = g.op(data[--r], vr);
      l >>= 1;
      r >>= 1;
    }
    return g.op(vl, vr);
  }
};
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  struct M {
    int const inf = 1 << 30;
    using T = pair<int, int>;
    [[nodiscard]] auto op(const T& a, const T& b) const -> T {
      return {min(a.first, a.second + b.first), a.second + b.second};
    }
    [[nodiscard]] auto e() const -> T { return {inf, 0}; }
  };
  int n, q;
  cin >> n >> q;
  string s;
  cin >> s;
  vector<int> a(n);
  for(int i = 0; i < n; i++) a[i] = s[i] == '(' ? 1 : -1;
  segtree seg(M{}, n);
  for(int i = 0; i < n; i++) seg.set(i, {a[i], a[i]});
  while(q--) {
    int t, l, r;
    cin >> t >> l >> r;
    l--;
    r--;
    if(t == 1) {
      swap(a[l], a[r]);
      seg.set(l, {a[l], a[l]});
      seg.set(r, {a[r], a[r]});
    } else {
      auto [mn, s] = seg[{l, r + 1}];
      cout << (mn >= 0 && s == 0 ? "Yes" : "No") << endl;
    }
  }
}
