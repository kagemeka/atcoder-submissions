#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for(int i = 0; i < n; ++i)
template<typename T, typename N> auto power(T x, N n) -> T {
  T y = 1;
  for(; n; x *= x, n >>= 1)
    if(n & 1) y *= x;
  return y;
}
template<typename T, int n> struct matrix {
  using Self = matrix;
  using A = array<array<T, n>, n>;
  A data;
  matrix(A a): data(a) {}
  matrix() { rep(i, n) data[i].fill(0); }
  matrix(int x) {
    assert(x == 0 || x == 1);
    *this = x == 0 ? Self() : e();
  }
  auto operator[](int i) -> array<T, n>& { return data[i]; }
  static auto e() -> Self {
    Self e;
    rep(i, n) e[i][i] = 1;
    return e;
  }
  auto operator*(Self& rhs) -> Self {
    Self a;
    rep(i, n) rep(k, n) rep(j, n) a[i][j] += data[i][k] * rhs[k][j];
    return a;
  }
  auto operator*=(Self& rhs) { *this = *this * rhs; }
};
auto main() -> int {
  int n;
  cin >> n;
  using pi = pair<long, long>;
  vector<pi> xy(n);
  for(int i = 0; i < n; i++) cin >> xy[i].first >> xy[i].second;
  int m;
  cin >> m;
  using mat = matrix<long, 3>;
  vector<mat> f(m + 1);
  f[0] = mat::e();
  rep(i, m) {
    int t;
    cin >> t;
    f[i + 1][2][2] = 1;
    if(t == 1) {
      f[i + 1][0][1] = 1;
      f[i + 1][1][0] = -1;
    }
    if(t == 2) {
      f[i + 1][0][1] = -1;
      f[i + 1][1][0] = 1;
    }
    if(t == 3) {
      int p;
      cin >> p;
      f[i + 1][0][0] = -1;
      f[i + 1][0][2] = 2 * p;
      f[i + 1][1][1] = 1;
    }
    if(t == 4) {
      int p;
      cin >> p;
      f[i + 1][0][0] = 1;
      f[i + 1][1][1] = -1;
      f[i + 1][1][2] = 2 * p;
    }
    f[i + 1] *= f[i];
  }
  int q;
  cin >> q;
  while(q--) {
    int a, b;
    cin >> a >> b;
    b--;
    auto& [x, y] = xy[b];
    mat v;
    v[0][0] = x;
    v[1][0] = y;
    v[2][0] = 1;
    v = f[a] * v;
    cout << v[0][0] << ' ' << v[1][0] << endl;
  }
}
