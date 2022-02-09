#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>


int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, k;
  std::cin >> n >> k;
  std::vector<int> r(n);
  for (int i = 0; i < n; i++) std::cin >> r[i];
  double rate = .0;
  std::sort(r.begin(), r.end(), std::greater<int>());
  for (int i = k - 1; i > -1; i--) {
    rate = (rate + r[i]) / 2;
  }
  std::cout << std::setprecision(8) << rate << '\n';
}
