#include <bits/stdc++.h>
using namespace std;
struct fenwick {
  vector<int> data;
  fenwick(int size): data(size + 1) {}
  auto size() -> int { return data.size() - 1; }
  auto add(int i, int x) {
    for(i++; i <= size(); i += i & -i) data[i] += x;
  }
  auto get(int i) -> int {
    int v = 0;
    for(; i > 0; i -= i & -i) { v += data[i]; }
    return v;
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
  // a_i -= k;
  // range sum >= 0;
  // s = cumsum(a) (1 indexed)
  // forall i=0..=n, count up j (i < j \land s_j >= s_i)
  // array_compression + fenwick
  int n, k;
  cin >> n >> k;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  vector<long> s(n + 1);
  for(int i = 0; i < n; i++) s[i + 1] = s[i] + a[i] - k;
  auto b = array_compression<long>::once(s);
  fenwick fw(n + 1);
  long cnt = 0;
  for(auto& x: b) {
    cnt += fw.get(x + 1);
    fw.add(x, 1);
  }
  cout << cnt << endl;
}
