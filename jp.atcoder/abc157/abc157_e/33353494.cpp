#include <bits/stdc++.h>
using namespace std;
auto bit_length(int n) -> int { return 32 - __builtin_clz(n); }
template<typename G> class segtree {
  using T = typename G::T;
  vector<T> data;
  G g;
  auto update(int i) { data[i] = g.op(data[i << 1], data[i << 1 | 1]); }
  auto n() -> int { return data.size() >> 1; }

public:
  int size;
  segtree(G g, int size): g(g), size(size) {
    assert(size > 0);
    int n = 1 << bit_length(size - 1);
    data.resize(n << 1, g.e());
  }
  auto set(int i, T x) {
    assert(0 <= i && i < size);
    for(data[i += n()] = x, i >>= 1; i >= 1; i >>= 1) update(i);
  }
  auto operator[](int i) -> T { return data[i + n()]; }
  auto operator[](pair<int, int> lr) -> T {
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
  struct G {
    using T = int;
    auto op(T x, T y) -> T { return x | y; }
    auto e() -> T { return 0; }
  };
  int n;
  string s;
  int q;
  cin >> n >> s >> q;
  vector<int> a(n);
  for(int i = 0; i < n; i++) a[i] = s[i] - 'a';
  segtree<G> seg(G{}, n);
  for(int i = 0; i < n; i++) { seg.set(i, 1 << a[i]); }
  while(q--) {
    int t;
    cin >> t;
    if(t == 1) {
      int i;
      char c;
      cin >> i >> c;
      i--;
      int j = c - 'a';
      seg.set(i, 1 << j);
    } else {
      int l, r;
      cin >> l >> r;
      l--;
      r--;
      cout << __builtin_popcount(seg[{l, r + 1}]) << endl;
    }
  }
}
