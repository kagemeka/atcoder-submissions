#include <bits/stdc++.h>

int dist(int a, int b, int c, int x) {
  return b * (x / (a + c) * a + std::min(x % (a + c), a));
}

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int a, b, c, d, e, f, x;
  std::cin >> a >> b >> c >> d >> e >> f >> x;

  int d0 = dist(a, b, c, x);
  int d1 = dist(d, e, f, x);
  std::cout << (d0 > d1    ? "Takahashi"
                : d0 == d1 ? "Draw"
                           : "Aoki")
            << std::endl;
}
