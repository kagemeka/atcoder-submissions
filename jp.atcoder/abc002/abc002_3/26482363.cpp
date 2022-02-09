#include <iostream>
#include <iomanip>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int x0, y0, x1, y1, x2, y2;
  std::cin >> x0 >> y0 >> x1 >> y1 >> x2 >> y2;
  x1 -= x0;
  y1 -= y0;
  x2 -= x0;
  y2 -= y0;
  double s = (double)std::abs(x1 * y2 - y1 * x2) / 2;
  std::cout << std::setprecision(8) << s << '\n';
}
