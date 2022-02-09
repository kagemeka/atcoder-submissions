#include <iostream>
#include <vector>
#include <limits>
#include <cassert>
#include <algorithm>
using namespace std;


namespace bit_matrix {
  constexpr uint mul_e = (1LL << 32) - 1;
  using Matrix = vector<vector<uint>>;
  Matrix identity(int n) {
    Matrix e(n, vector<uint>(n));
    for (int i = 0; i < n; i++) e[i][i] = mul_e;
    return e;
  }

  Matrix dot(const Matrix &a, const Matrix &b) {
    int h = a.size(), w = a[0].size(), y = b.size(), x = b[0].size();
    assert(w == y);
    Matrix c(h, vector<uint>(x));
    for (int i = 0; i < h; i++) {
      for (int j = 0; j < x; j++) {
        for (int k = 0; k < w; k++) {
          c[i][j] ^= a[i][k] & b[k][j];
        }
      }
    }
    return c;
  }

  template <typename T>
  Matrix pow(Matrix x, T n) {
    Matrix y = identity(x.size());
    while (n) {
      if (n & 1) y = dot(y, x);
      x = dot(x, x);
      n >>= 1;
    }
    return y;
  }
};


int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, k; cin >> n >> k;
  vector<vector<uint>> a(n, vector<uint>(1));
  vector<vector<uint>> c(n, vector<uint>(n));
  for (int i = 0; i < n; i++) cin >> a[i][0];
  for (int i = 0; i < n; i++) cin >> c[0][i];
  for (int i = 0; i < n - 1; i++) c[i + 1][i] = bit_matrix::mul_e;

  if (k <= n) {
    cout << a[k - 1][0] << '\n';
  }
  c = bit_matrix::pow(c, k - n);
  reverse(a.begin(), a.end());
  a = bit_matrix::dot(c, a);
  cout << a[0][0] << '\n';
}
