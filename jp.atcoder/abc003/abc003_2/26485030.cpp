#include <iostream>
#include <string>
#include <set>


int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::string s, t;
  std::set<char> atcoder = {'a', 't', 'c', 'o', 'd', 'e', 'r'};

  std::cin >> s >> t;
  for (int i = 0; i < (int)s.size(); i++) {
    if (s[i] == t[i]) continue;
    if (s[i] == '@' and atcoder.count(t[i])) continue;
    if (t[i] == '@' and atcoder.count(s[i])) continue;
    std::cout << "You will lose" << '\n';
    return 0;
  }
  std::cout << "You can win" << '\n';
}
