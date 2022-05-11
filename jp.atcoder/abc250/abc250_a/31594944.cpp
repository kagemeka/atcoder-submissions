#include <bits/stdc++.h>

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int h, w, r, c;
  std::cin >> h >> w >> r >> c;
  std::cout << 4 - (r == 1) - (r == h) - (c == 1) - (c == w) << std::endl;
}
