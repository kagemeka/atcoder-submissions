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
class fw_multiset {
  fenwick<int> fw;

public:
  fw_multiset(int less_than): fw(less_than) {}
  auto size() -> int { return fw.get(fw.size()); }
  auto count(int x) -> int { return fw.get(x + 1) - fw.get(x); }
  auto insert(int x, int count = 1) { fw.operate(x, count); }
  auto remove(int x, int count = 1) { fw.operate(x, -count); }
  auto lower_bound(int x) -> int { return fw.get(x); }
  auto upper_bound(int x) -> int { return fw.get(x + 1); }
  auto operator[](int i) -> int {
    return fw.max_right([&](int x) { return x <= i; });
  }
};
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  // lowercases are only 26 kinds.
  int n;
  string s;
  int q;
  cin >> n >> s >> q;
  // f(r) - f(l - 1)
  // ordered set, fenwick, segtree.
  vector<int> a(n);
  for(int i = 0; i < n; i++) a[i] = s[i] - 'a';
  int const k = 26;
  vector<fw_multiset> indices(k, fw_multiset(n));
  for(int i = 0; i < n; i++) { indices[a[i]].insert(i); }
  while(q--) {
    int t;
    cin >> t;
    if(t == 1) {
      int i;
      char c;
      cin >> i >> c;
      i--;
      int j = c - 'a';
      indices[a[i]].remove(i);
      a[i] = j;
      indices[j].insert(i);
    } else {
      int l, r;
      cin >> l >> r;
      l--;
      r--;
      int cnt = 0;
      for(int i = 0; i < k; i++) {
        cnt += indices[i].upper_bound(r) != indices[i].upper_bound(l - 1);
      }
      cout << cnt << endl;
    }
  }
}
