#include <iostream>
#include <string>
#include <locale>


int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  std::string s; std::cin >> s;
  s[0] = std::toupper(s[0]);
  for (int i = 1; i < s.size(); i++) s[i] = std::tolower(s[i]);
  std::cout << s << '\n';

}
