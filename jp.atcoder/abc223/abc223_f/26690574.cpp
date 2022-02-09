template <typename T>
int bit_length(T n) {
  int l = 0;
  while (1 << l <= n) ++l;
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

  int n, q;
  std::string s;
  std::cin >> n >> q >> s;
  std::vector<int> a(n);
  for (int i = 0; i < n; i++) {a[i] = s[i] == '(' ? 1 : -1;}
  std::vector<int> b(n + 1);
  for (int i = 0; i < n; i++) b[i + 1] = b[i] + a[i];
  auto e_s = [](){ return 1 << 30; };
  auto op_s = [](int a, int b){ return std::min(a, b); };
  auto e_f = [](){ return 0; };
  auto op_f = [](int f, int g){ return f + g; };
  auto map = [](int f, int x){ return x + f; };
  auto ms = Monoid<int>{op_s, e_s, true};
  auto mf = Monoid<int>{op_f, e_f, true};
  auto cfg = SegmentTreeLazyConfig<int, int>{ms, mf, map};
  auto seg = SegmentTreeLazy<int, int>(cfg, b);

  while (q--) {
    int t, l, r;
    std::cin >> t >> l >> r;
    --l; --r;
    if (t == 1) {
      seg.set(l + 1, r + 1, a[r] - a[l]);
      std::swap(a[l], a[r]);
    } else {
      int base = seg.get(l, l + 1);
      int tot = seg.get(r + 1, r + 2) - base;
      int mn = seg.get(l, r + 2) - base;
      std::cout << (tot == 0 && mn >= 0 ? "Yes" : "No") << '\n';
    }
  }
}
