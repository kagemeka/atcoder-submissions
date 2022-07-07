
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
    int d = 1 << (int)(log2(n + 1) + 1);
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

class fenwick_multiset {
  fenwick<int> fw;

public:
  fenwick_multiset(int size): fw(size) {}

  auto insert(int x) { fw.operate(x, 1); }

  auto remove(int x) { fw.operate(x, -1); }

  auto remove_all(int x) { fw.operate(x, fw.get(x) - fw.get(x + 1)); }

  auto lower_bound(int x) -> int { return fw.get(x); }

  auto upper_bound(int x) -> int { return fw.get(x + 1); }

  auto operator[](int i) -> int {
    return fw.max_right([&](int x) { return x <= i; });
  }
};

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;
  vector<int> p(n), index(n);
  for(int i = 0; i < n; i++) {
    cin >> p[i];
    p[i]--;
    index[p[i]] = i;
  }

  fenwick_multiset s(n + 2);

  s.insert(0);
  s.insert(0);
  s.insert(n + 1);
  s.insert(n + 1);

  long tot = 0;
  for(int x = n; x > 0; x--) {
    int i = index[x - 1] + 1;
    s.insert(i);
    int k = s.lower_bound(i);
    int j0 = s[k - 2], j1 = s[k - 1], j2 = s[k + 1], j3 = s[k + 2];
    tot += (long)x * (j1 - j0) * (j2 - i);
    tot += (long)x * (i - j1) * (j3 - j2);
  }
  cout << tot << endl;
}
