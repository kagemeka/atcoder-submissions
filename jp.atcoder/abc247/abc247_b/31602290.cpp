#include <bits/stdc++.h>

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  using namespace std;

  int n;
  cin >> n;
  vector<string> s(n), t(n);
  for (int i = 0; i < n; i++) {
    cin >> s[i] >> t[i];
  }

  auto check = [&](int i) -> bool {
    for (int j = 0; j < n; j++) {
      if (i == j)
        continue;
      if (s[i] == s[j] || s[i] == t[j])
        return false;
    }
    return true;
  };

  for (int i = 0; i < n; i++) {
    for (int k = 0; k < 2; k++) {
      if (check(i))
        continue;
      swap(s, t);
      if (check(i))
        continue;
      cout << "No" << '\n';
      return 0;
    }
  }

  cout << "Yes" << '\n';
}
