#include <iostream>
#include <string>
#include <locale>
#include <algorithm>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  std::string s; std::cin >> s;
  s[0] = std::toupper(s[0]);
  std::transform(next(s.begin()), s.end(), next(s.begin()),::tolower);
  std::cout << s << '\n';

}
