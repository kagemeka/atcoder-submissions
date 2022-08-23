#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for(int i = 0; i < n; ++i)
template<typename T, int n> struct matrix {
  using Self = matrix;
  array<array<T, n>, n> data;
  matrix() { rep(i, n) data[i].fill(0); }
  matrix(int x): matrix() {
    assert(x == 0 || x == 1);
    if(x) { rep(i, n) data[i][i] = 1; }
  }
  auto operator[](int i) -> array<T, n>& { return data[i]; }
  auto operator*(Self& rhs) -> Self {
    Self a;
    rep(i, n) rep(k, n) rep(j, n) a[i][j] += data[i][k] * rhs[k][j];
    return a;
  }
  auto operator*=(Self& rhs) { *this = *this * rhs; }
  auto operator+(Self& rhs) -> Self {
    Self a(*this);
    rep(i, n) rep(j, n) a[i][j] += rhs[i][j];
    return a;
  }
  auto operator+=(Self& rhs) { *this = *this + rhs; }
  auto debug() { rep(i, n) rep(j, n) cout << data[i][j] << " \n"[j == n - 1]; }
};
template<typename T, typename Z> auto power(T x, Z n) -> T {
  // if(n < 0) {
  //   x = 1 / x;
  //   n *= -1;
  // }
  T y = 1;
  for(; n; x *= x, n >>= 1)
    if(n & 1) y *= x;
  return y;
}
uint const one = (1l << 31) - 1;
struct R {
  uint v;
  R() = default;
  R(uint x): v(x) {}
  R(int x) {
    assert(x == 0 || x == 1);
    v = one * x;
  }
  auto operator*(R rhs) -> R { return R{v & rhs.v}; }
  auto operator+(R rhs) -> R { return R{v ^ rhs.v}; }
  auto operator+=(R rhs) { *this = *this + rhs; }
};
auto main() -> int {
  int n, m;
  cin >> n >> m;
  using mat = matrix<R, 100>;
  mat a;
  mat b;
  for(int i = 0; i < n; i++) {
    uint x;
    cin >> x;
    a[n - 1 - i][0] = R{x};
  }
  for(int i = 0; i < n; i++) {
    uint x;
    cin >> x;
    b[0][i] = R{x};
  }
  for(int i = 0; i < n - 1; i++) b[i + 1][i] = 1;
  b = power(b, m - 1);
  a = b * a;
  cout << a[n - 1][0].v << endl;
}
