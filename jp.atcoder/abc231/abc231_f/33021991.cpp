#include <bits/stdc++.h>
using namespace std;

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

template<typename T> class fenwick {
  vector<T> d;

public:
  fenwick(int size): d(size + 1) {}

  auto size() -> int { return d.size() - 1; }

  auto operate(int i, T x) -> void {
    assert(0 <= i && i < size());
    i++;
    while(i <= size()) {
      d[i] += x;
      i += i & -i;
    }
  }

  auto get(int i) -> T {
    assert(0 <= i && i <= size());
    T v = 0;
    while(i > 0) {
      v += d[i];
      i -= i & -i;
    }
    return v;
  }
};

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;
  using p = pair<int, int>;
  vector<p> ab(n);
  for(int i = 0; i < n; i++) cin >> ab[i].first;
  for(int i = 0; i < n; i++) cin >> ab[i].second;

  sort(ab.begin(), ab.end(), [](p const& x, p const& y) {
    if(x.first != y.first) { return x.first < y.first; }
    return x.second > y.second;
  });

  // long tot = 0;
  // long cnt = 1;
  // for(int i = 0; i < n - 1; i++) {
  //   if(ab[i] == ab[i + 1]) cnt += 1;
  //   else {
  //     tot += cnt * (cnt - 1) / 2;
  //     cnt = 1;
  //   }
  // }
  // tot += cnt * (cnt - 1) / 2;

  // vector<int> b(n);
  // for(int i = 0; i < n; i++) b[i] = ab[i].second;

  // b = array_compression<int>::once(b);

  // fenwick<int> fw(n + 10);

  // for(int i = 0; i < n; i++) {
  //   tot += i + 1 - fw.get(b[i]);
  //   fw.operate(b[i], 1);
  // }
  // cout << tot << endl;
}