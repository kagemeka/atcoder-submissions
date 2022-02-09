#include <iostream>
#include <set>


int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n; std::cin >> n;

  std::set<int> ng;
  for (int i = 0; i < 3; i++) {
    int x; std::cin >> x;
    ng.insert(x);
  }

  if (ng.count(n)) {
    std::cout << "NO" << '\n';
    return 0;
  }
  for (int i = 0; i < 100; i++) {
    bool ok = false;
    for (int j = 3; j > 0; j--) {
      if (ng.count(n - j)) continue;
      ok = true;
      n -= j;
      break;
    }
    if (!ok) {
      std::cout << "NO" << '\n';
      return 0;
    }
    if (n <= 0) {
      std::cout << "YES" << '\n';
      return 0;
    }
  }
  std::cout << "NO" << '\n';
}
