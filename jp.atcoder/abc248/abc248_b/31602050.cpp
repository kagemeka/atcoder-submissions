#include <bits/stdc++.h>

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int a, b, k;
  std::cin >> a >> b >> k;

  int cnt = 0;
  while (b / a >= k) {
    a *= k;
    ++cnt;
  }
  cnt += a < b;
  std::cout << cnt << '\n';
}
