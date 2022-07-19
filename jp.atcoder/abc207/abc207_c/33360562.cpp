#include <bits/stdc++.h>
using namespace std;
template<typename T> class fenwick {
  vector<T> data;

public:
  fenwick(int size): data(size + 1) {}
  auto size() -> int { return data.size() - 1; }
  auto operate(int i, T x) -> void {
    assert(0 <= i);
    for(i++; i <= size(); i += i & -i) data[i] += x;
  }
  auto get(int i) -> T {
    T v = 0;
    for(; i > 0; i -= i & -i) v += data[i];
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
      auto nv = v + data[i + d];
      if(f(nv)) {
        i += d;
        v = nv;
      }
    }
  }
};
template<typename A> auto unique(A a) -> A {
  sort(a.begin(), a.end());
  a.erase(std::unique(a.begin(), a.end()), a.end());
  return a;
}
template<typename T> class array_compression {
  vector<T> values;

public:
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
  using p = pair<int, int>;
  vector<p> segments(n);
  vector<int> coords;
  coords.resize(n * 2);
  for(int i = 0; i < n; i++) {
    int t, l, r;
    cin >> t >> l >> r;
    l *= 2;
    r *= 2;
    if(t == 1 || t == 3) r++;
    if(t == 3 || t == 4) l++;
    segments[i] = {l, r};
    coords.push_back(l);
    coords.push_back(r);
  }
  array_compression<int> f(coords);
  sort(segments.begin(), segments.end(), [&](auto& x, auto& y) {
    auto& [l0, r0] = x;
    auto& [l1, r1] = y;
    return l0 != l1 ? l0 < l1 : r0 > r1;
  });
  fenwick<int> fw(2 * n);
  long cnt = 0;
  for(int i = 0; i < n; i++) {
    auto& [l, r] = segments[i];
    l = f(l);
    r = f(r);
    cnt += i - fw.get(l + 1);
    fw.operate(r, 1);
  }
  cout << cnt << endl;
}
