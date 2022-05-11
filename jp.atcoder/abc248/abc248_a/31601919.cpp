#include <bits/stdc++.h>

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);

  std::string s;
  std::cin >> s;

  std::sort(s.begin(), s.end());
  for (int i = 0; i < 9; i++) {
    if (s[i] - '0' == i)
      continue;
    std::cout << i << std::endl;
    return 0;
  }
  std::cout << 9 << '\n';
}
