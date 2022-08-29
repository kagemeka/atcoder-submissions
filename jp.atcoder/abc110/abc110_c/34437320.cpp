#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s, t;
  cin >> s >> t;
  vector<int> f(26, -1), g(26, -1);
  int n = s.size();
  for(int i = 0; i < n; i++) {
    int x = s[i] - 'a';
    int y = t[i] - 'a';
    if(f[x] == -1 && g[y] == -1) {
      f[x] = y;
      g[y] = x;
      continue;
    } else if(f[x] == y) {
      continue;
    }
    cout << "No" << '\n';
    return 0;
  }
  cout << "Yes" << '\n';
}
