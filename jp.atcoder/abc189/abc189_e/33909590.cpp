#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for(int i = 0; i < n; ++i)
template<typename T, typename N> auto power(T x, N n) -> T {
  T y = 1;
  for(; n; x *= x, n >>= 1)
    if(n & 1) y *= x;
  return y;
}
template<typename T, int n> struct matrix {
  using Self = matrix;
  array<array<T, n>, n> data;
  matrix() { rep(i, n) data[i].fill(0); }
  matrix(int x): matrix() {
    assert(x == 0 || x == 1);
    if(x) { rep(i, n) data[i][i] = 1; }
  }
  auto operator[](int i) -> array<T, n>& { return data[i]; }
  auto operator*(Self& rhs) -> Self {
    Self a;
    rep(i, n) rep(k, n) rep(j, n) a[i][j] += data[i][k] * rhs[k][j];
    return a;
  }
  auto operator*=(Self& rhs) { *this = *this * rhs; }
  auto print() {
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < n; j++) { cout << data[i][j] << " \n"[j == n - 1]; }
    }
  }
};
template<typename G> class segtree {
  using T = typename G::T;
  vector<T> data;
  G g;
  auto merge(int i) { data[i] = g.op(data[i << 1], data[i << 1 | 1]); }
  auto n() -> int { return data.size() >> 1; }

public:
  int size;
  segtree(G g, int size): g(g), size(size) {
    assert(size > 0);
    int n = 1 << (32 - __builtin_clz(size - 1));
    data.resize(n << 1, g.e());
  }
  auto set(int i, T x) {
    assert(0 <= i && i < size);
    for(data[i += n()] = x, i >>= 1; i >= 1; i >>= 1) merge(i);
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
  template<typename F> auto max_right(F f, int l) const -> int {
    assert(0 <= l && l <= size);
    if(l == size) return size;
    T v = g.e();
    int i = l + n();
    while(true) {
      i /= i & -i;
      T nv = g.op(v, data[i]);
      if(!f(nv)) break;
      v = nv;
      i++;
      if(__builtin_popcount(i) == 1) return size;
    }
    while(i < n()) {
      i <<= 1;
      T nv = g.op(v, data[i]);
      if(!f(nv)) continue;
      v = nv;
      i++;
    }
    return i - n();
  }
  template<typename F> auto min_left(F f, int r) const -> int {
    assert(0 <= r && r <= size);
    if(r == 0) return 0;
    T v = g.e();
    int i = r + n();
    while(true) {
      i /= i & -i;
      T nv = g.op(data[i - 1], v);
      if(!f(nv)) break;
      i--;
      v = nv;
      if(__builtin_popcount(i) == 1) return 0;
    }
    while(i < n()) {
      i <<= 1;
      T nv = g.op(data[i - 1], v);
      if(!f(nv)) continue;
      i--;
      v = nv;
    }
    return i - n();
  }
};
auto main() -> int {
  int n;
  cin >> n;
  using pi = pair<long, long>;
  vector<pi> xy(n);
  for(int i = 0; i < n; i++) cin >> xy[i].first >> xy[i].second;
  int m;
  cin >> m;
  using mat = matrix<long, 3>;
  vector<mat> f(m + 1);
  f[0] = 1;
  rep(i, m) {
    int t;
    cin >> t;
    f[i + 1][2][2] = 1;
    if(t == 1) {
      f[i + 1][0][1] = 1;
      f[i + 1][1][0] = -1;
    }
    if(t == 2) {
      f[i + 1][0][1] = -1;
      f[i + 1][1][0] = 1;
    }
    if(t == 3) {
      int p;
      cin >> p;
      f[i + 1][0][0] = -1;
      f[i + 1][0][2] = 2 * p;
      f[i + 1][1][1] = 1;
    }
    if(t == 4) {
      int p;
      cin >> p;
      f[i + 1][0][0] = 1;
      f[i + 1][1][1] = -1;
      f[i + 1][1][2] = 2 * p;
    }
  }
  struct M {
    using T = mat;
    auto op(T& a, T& b) -> T { return b * a; }
    auto e() -> T { return 1; }
  };
  segtree seg(M{}, m + 1);
  for(int i = 0; i < m + 1; i++) { seg.set(i, f[i]); }
  int q;
  cin >> q;
  while(q--) {
    int a, b;
    cin >> a >> b;
    b--;
    auto& [x, y] = xy[b];
    mat v;
    v[0][0] = x;
    v[1][0] = y;
    v[2][0] = 1;
    v = seg[{0, a + 1}] * v;
    cout << v[0][0] << ' ' << v[1][0] << endl;
  }
}
