#include <iostream>
#include <vector>
#include <iomanip>



std::vector<std::vector<double>> binom_pascal(int n) {
  std::vector<std::vector<double>> p(n, std::vector<double>(n, 0));
  for (int i = 0; i < n; i++) p[i][0] = 1;
  for (int i = 1; i < n; i++) {
    for (int j = 1; j <= i; j++) {
      p[i][j] = p[i - 1][j] + p[i - 1][j - 1] / 4;
    }
  }
  return p;
}



int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, d, x, y;
  std::cin >> n >> d >> x >> y;
  x = std::abs(x);
  y = std::abs(y);

  if (y % d || x % d) {
    std::cout << 0 << '\n';
    return 0;
  }
  x /= d;
  y /= d;
  if (x + y > n || (n - x - y) & 1) {
    std::cout << 0 << '\n';
    return 0;
  }

  auto p = binom_pascal(1 << 10);
  double res = .0;
  int k = n - x - y;
  for (int i = 0; i <= k; i += 2) {
    int d = i / 2;
    int u = y + d;
    int l = (k - i) / 2;
    int r = x + l;
    res += p[n][u] * p[n - u][d] * p[n - u - d][l] * p[n - u - d - l][r];
  }
  std::cout << std::setprecision(16) << res << '\n';

}
