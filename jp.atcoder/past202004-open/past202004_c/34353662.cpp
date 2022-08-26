#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<string> s(n);
  for(int i = 0; i < n; i++) cin >> s[i];
  for(int i = n - 2; i >= 0; i--) {
    for(int j = 1; j < 2 * n - 2; j++) {
      if(s[i][j] != '#') continue;
      for(int d = -1; d < 2; d++) {
        if(s[i + 1][j + d] == 'X') s[i][j] = 'X';
      }
    }
  }
  for(auto& s: s) cout << s << endl;
}
