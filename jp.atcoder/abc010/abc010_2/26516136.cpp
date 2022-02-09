#include <iostream>


int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n; std::cin >> n;
  int cnt = 0;
  while (n--) {
    int a; std::cin >> a;
    while (a % 2 == 0 || a % 3 == 2) { a--; ++cnt; }
  }
  std::cout << cnt << '\n';

}
