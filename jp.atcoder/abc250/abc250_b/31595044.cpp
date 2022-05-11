#include <bits/stdc++.h>

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, a, b;
  std::cin >> n >> a >> b;

  for (int i = 0; i < n * a; i++) {
    for (int j = 0; j < n * b; j++) {
      char c = ((i / a) ^ (j / b)) & 1 ? '#' : '.';
      std::cout << c << " ";
    }
    std::cout << std::endl;
  }
}
