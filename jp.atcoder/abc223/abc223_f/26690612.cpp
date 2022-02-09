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


template <typename S>
class SegmentTree {
private:
  using M = Monoid<S>;
  M m;
  int size, n;
  std::vector<S> data;

  void merge(int i) { data[i] = m.op(data[i << 1], data[i << 1 | 1]); }

public:
  SegmentTree(M m, const std::vector<S> &a) : m(m), size((int)a.size()) {
    n = 1 << bit_length(size - 1);
    data = std::vector<S>(n << 1, m.e());
    for (int i = 0; i < size; i++) data[n + i] = a[i];
    for (int i = n - 1; i > 0; --i) merge(i);
  }
  SegmentTree(M m, int n) : SegmentTree(m, std::vector<S>(n, m.e())) {}

  void set(int i, S x) {
    assert(0 <= i && i < size);
    i += n;
    data[i] = x;
    while (i > 1) { i >>= 1; merge(i); }
  }

  const S& operator[](int i) const {
    assert(0 <= i && i < size);
    return data[n + i];
  }

  S get(int l, int r) const {
    assert(0 <= l && l <= r && r <= size);
    l += n; r += n;
    S vl = m.e(), vr = m.e();
    while (l < r) {
      if (l & 1) vl = m.op(vl, data[l++]);
      if (r & 1) vr = m.op(data[--r], vr);
      l >>= 1; r >>= 1;
    }
    return m.op(vl, vr);
  }

  int max_right(std::function<bool(S)> is_ok, int l) const {
    assert(0 <= l < size);
    S v = m.e();
    int i = n + l;
    while (true) {
      i /= i & -i;
      if (is_ok(m.op(v, data[i]))) {
        v = m.op(v, data[i]);
        i++;
        if (i & -i == i) return size;
        continue;
      }
      while (i < n) {
        i <<= 1;
        if (!is_ok(m.op(v, data[i]))) continue;
        v = m.op(v, data[i++]);
      }
      return i - n;
    }
  }
};


int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, q;
  std::string s;
  std::cin >> n >> q >> s;
  std::vector<int> a(n);
  for (int i = 0; i < n; i++) { a[i] = s[i] == '(' ? 1 : -1; }
  using P = std::pair<int, int>;
  auto op = [](P a, P b) -> P {
    return std::make_pair(a.first + b.first, std::min(a.second, a.first + b.second));
  };
  auto e = []() -> P { return std::make_pair(0, 1 << 20); };
  Monoid<P> m{op, e, false};

  std::vector<P> b(n);
  for (int i = 0; i < n; i++) b[i] = std::make_pair(a[i], a[i]);
  auto seg = SegmentTree<P>(m, b);

  while (q--) {
    int t, l, r;
    std::cin >> t >> l >> r;
    --l; --r;
    if (t == 1) {
      seg.set(l, b[r]);
      seg.set(r, b[l]);
      swap(b[l], b[r]);
    } else {
      P res = seg.get(l, r + 1);
      std::cout << (res.first == 0 && res.second >= 0 ? "Yes" : "No") << '\n';
    }
  }
}
