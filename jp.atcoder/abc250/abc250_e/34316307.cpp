#include <bits/stdc++.h>
using namespace std;
template<typename T> void print(vector<T> v) {
  for(int i = 0; i < (int)v.size(); ++i) {
    cout << v[i] << " \n"[i == (int)v.size() - 1];
  }
}
template<typename T, unsigned long N> void print(array<T, N> v) {
  for(unsigned long i = 0; i < N; ++i) { cout << v[i] << " \n"[i == N - 1]; }
}
template<typename T> void print(const T& v) { cout << v << '\n'; }
template<typename T, typename... U> void print(const T& t, const U&... args) {
  cout << t << ' ';
  print(args...);
}
template<typename T, typename... U>
void print(char sep, const T& t, const U&... args) {
  if(sizeof...(args) > 0) {
    cout << t << sep;
    print(sep, args...);
  } else {
    print(t);
  }
}
#ifdef CPP_DEBUG // g++ -DCPP_DEBUG ...
#define debug(...) print(__VA_ARGS__);
#else
#define debug(...) nullptr
#endif
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n), b(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  for(int i = 0; i < n; i++) cin >> b[i];
  map<int, int> id;
  set<int> bs;
  for(int i = 0; i < n; i++) {
    int& x = a[i];
    if(id.count(x)) {
      x = a[i - 1];
    } else {
      x = id[x] = id.size() + 1;
    }
    int& y = b[i];
    if(bs.count(y) || !id.count(y)) {
      y = b[i - 1];
    } else {
      bs.insert(y);
      y = b[i - 1] + 1;
    }
  }
  debug(a);
  debug(b);
  int const inf = 1 << 30;
  vector<int> c(n);
  for(int i = 0; i < n; i++) { c[i] = id.count(b[i]) ? id[b[i]] : inf; }
  for(int i = 0; i < n - 1; i++) c[i + 1] = max(c[i + 1], c[i]);
  int q;
  cin >> q;
  while(q--) {
    int i, j;
    cin >> i >> j;
    i--;
    j--;
    cout << (a[i] == b[j] && b[j] == c[j] ? "Yes" : "No") << '\n';
  }
}
