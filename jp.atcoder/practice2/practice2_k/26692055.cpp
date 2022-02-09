template <typename T>
int bit_length(T n) {
  int l = 0;
  while (1LL << l <= n) ++l;
  return l;
}

#include <functional>

template <typename S>
struct Monoid {
private:
  using Op = std::function<S(S, S)>;
  using Id = std::function<S()>;
public:
  Op op;
  Id e;
  bool commutative;
};


#include <iostream>
#include <vector>
#include <cassert>
#include <functional>


template <typename S, typename F>
struct SegmentTreeLazyConfig {
  Monoid<S> s;
  Monoid<F> f;
  std::function<S(F, S)> map;
};


template <typename S, typename F>
class SegmentTreeLazy {
private:
  using C = SegmentTreeLazyConfig<S, F>;
  C c;
  int size, n, h;
  std::vector<S> data;
  std::vector<F> lazy;

  void merge(int i) { data[i] = c.s.op(data[i << 1], data[i << 1 | 1]); }

  void apply(int i, F f) {
    data[i] = c.map(f, data[i]);
    if (i < n) lazy[i] = c.f.op(f, lazy[i]);
  }

  void propagate(int i) {
    apply(i << 1, lazy[i]);
    apply(i << 1 | 1, lazy[i]);
    lazy[i] = c.f.e();
  }

public:
  SegmentTreeLazy(C c, const std::vector<S> &a) : c(c), size((int)a.size()) {
    n = 1 << bit_length(size - 1);
    h = bit_length(n);
    data = std::vector<S>(n << 1, c.s.e());
    for (int i = 0; i < size; i++) data[n + i] = a[i];
    lazy = std::vector<F>(n, c.f.e());
    for (int i = n - 1; i > 0; --i) merge(i);
  }

  SegmentTreeLazy(C c, int n) : SegmentTreeLazy(c, std::vector<S>(n, c.s.e())) {}

  void set(int l, int r, F f) {
    assert(0 <= l && l <= r && r <= size);
    l += n; r += n;
    for (int i = h; i > -1; --i) {
      if ((l >> i) << i != l) propagate(l >> i);
      if ((r >> i) << i != r) propagate((r - 1) >> i);
    }
    int l0 = l, r0 = r;
    while (l < r) {
      if (l & 1) apply(l++, f);
      if (r & 1) apply(--r, f);
      l >>= 1; r >>= 1;
    }
    l = l0, r = r0;
    for (int i = 1; i < h + 1; i++) {
      if ((l >> i) << i != l) merge(l >> i);
      if ((r >> i) << i != r) merge((r - 1) >> i);
    }
  }

  S get(int l, int r) {
    assert(0 <= l && l <= r && r <= size);
    l += n; r += n;
    for (int i = h; i > -1; --i) {
      if ((l >> i) << i != l) propagate(l >> i);
      if ((r >> i) << i != r) propagate((r - 1) >> i);
    }
    S vl = c.s.e(), vr = c.s.e();
    while (l < r) {
      if (l & 1) vl = c.s.op(vl, data[l++]);
      if (r & 1) vr = c.s.op(data[--r], vr);
      l >>= 1; r >>= 1;
    }
    return c.s.op(vl, vr);
  }

  void update(int i, S x) {
    assert(0 <= i && i < size);
    i += n;
    for (int j = h; j > -1; j--) propagate(i >> j);
    data[i] = x;
    for (int j = 1; j < h + 1; j++) merge(i >> j);
  }
};


int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  const int MOD = 998244353;
  auto op_s = [](long long a, long long b) -> long long {
    long long a1, a0, b1, b0, c1, c0;
    long long mask = (1 << 30) - 1;
    a1 = a >> 30; a0 = a & mask;
    b1 = b >> 30; b0 = b & mask;
    c1 = (a1 + b1) % MOD; c0 = a0 + b0;
    return (c1 << 30) + c0;
  };
  auto e_s = []() -> long long { return 0LL; };
  auto op_f = [](long long f, long long g) -> long long {
    long long f1, f0, g1, g0, h1, h0;
    long long mask = (1 << 30) - 1;
    f1 = f >> 30; f0 = f & mask;
    g1 = g >> 30; g0 = g & mask;
    h1 = f1 * g1 % MOD; h0 = (f1 * g0 + f0) % MOD;
    return (h1 << 30) + h0;
  };
  auto e_f = []() -> long long { return 1LL << 30; };
  auto map = [](long long f, long long x) -> long long {
    long long f1, f0, x1, x0, y1, y0;
    long long mask = (1 << 30) - 1;
    f1 = f >> 30; f0 = f & mask;
    x1 = x >> 30; x0 = x & mask;
    y0 = x0;
    y1 = (f1 * x1 + f0 * x0) % MOD;
    return (y1 << 30) + y0;
  };
  auto ms = Monoid<long long>{op_s, e_s, true};
  auto mf = Monoid<long long>{op_f, e_f, false};
  auto cfg = SegmentTreeLazyConfig<long long, long long>{ms, mf, map};
  int n, q;
  std::cin >> n >> q;
  std::vector<long long> a(n);
  for (int i = 0; i < n; i++) {
    std::cin >> a[i];
    a[i] = (a[i] << 30) + 1;
  }
  auto seg = SegmentTreeLazy<long long, long long>(cfg, a);

  int t, l, r, b, c;
  while (q--) {
    std::cin >> t;
    if (t == 0) {
      std::cin >> l >> r >> b >> c;
      seg.set(l, r, ((long long)b << 30) + c);
    } else {
      std::cin >> l >> r;
      std::cout << (seg.get(l, r) >> 30) << '\n';
    }
  }
}
