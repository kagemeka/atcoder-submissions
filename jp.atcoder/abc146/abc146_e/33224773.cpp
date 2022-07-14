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
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  // s[j] - s[j] = j - i (mod k)
  int n, k;
  cin >> n >> k;
  vector<int> s(n + 1);
  for(int i = 0; i < n; i++) cin >> s[i + 1];
  for(int i = 0; i < n; i++) {
    s[i + 1] += s[i];
    s[i + 1] %= k;
  }
  for(int i = 0; i < n + 1; i++) s[i] = ((s[i] - i) % k + k) % k;
  s = array_compression<int>::once(s);
  int m = *max_element(s.begin(), s.end()) + 1;
  vector<int> cnt(m);
  long tot = 0;
  for(int i = 0, j = 0; i < n + 1; i++) {
    for(; j <= i - k; j++) cnt[s[j]]--;
    tot += cnt[s[i]];
    cnt[s[i]]++;
  }
  cout << tot << endl;
}
