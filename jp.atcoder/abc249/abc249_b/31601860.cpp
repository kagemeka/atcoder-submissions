#include <bits/stdc++.h>

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);

  std::string s;
  std::cin >> s;

  int n = s.size();
  std::sort(s.begin(), s.end());
  bool ok = true;
  if (std::islower(s[0]))
    ok = false;
  if (std::isupper(s[n - 1]))
    ok = false;
  for (int i = 0; i < n - 1; i++) {
    ok &= s[i] != s[i + 1];
  }
  std::cout << (ok ? "Yes" : "No") << std::endl;
}
