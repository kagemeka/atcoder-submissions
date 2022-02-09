#include <iostream>
#include <math.h>


int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int sx, sy, gx, gy, t, v;
  std::cin >> sx >> sy >> gx >> gy >> t >> v;
  int n; std::cin >> n;

  bool ok = true;
  while (n--) {
    int x, y; std::cin >> x >> y;
    double d1 = std::sqrt((x - sx) * (x - sx) + (y - sy) * (y - sy));
    double d2 = std::sqrt((gx - x) * (gx - x) + (gy - y) * (gy - y));
    if (d1 + d2 <= t * v) ok = false;
  }
  std::cout << (ok ? "NO" : "YES") << '\n';
}
