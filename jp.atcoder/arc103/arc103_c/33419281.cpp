#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s;
  cin >> s;
  int n = s.size();
  auto solve = [&]() -> bool {
    if(s[n - 1] == '1') return false;
    for(int i = 0; i < n - 1; i++) {
      if(s[i] != s[n - 2 - i]) return false;
    }
    if(s[0] == '0') return false;
    int p = n - 1;
    for(int i = n - 2; i >= 0; i--) {
      cout << i + 1 << ' ' << p + 1 << endl;
      if(s[i] == '1') p = i;
    }
    return true;
  };
  if(!solve()) { cout << -1 << endl; }
}
