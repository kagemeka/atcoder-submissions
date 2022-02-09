#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  string s, t;
  cin >> s >> t;
  int n = s.size(), m = t.size();
  for (int i = n - m; i > - 1; i--) {
    bool flag = true;
    for (int j = 0; j < m; j++) {
      if (s[i+j] != t[j] && s[i+j] != '?') {
        flag = false;
        break;
      }
    }
    if (flag) {
      for (int j = 0; j < m; j++) {
        s[i+j] = t[j];
      }
      for (int j = 0; j < n; j++) {
        if (s[j] == '?') s[j] = 'a';
      }
      cout << s << '\n';
      return 0;
    }
  }
  cout << "UNRESTORABLE" << '\n';
  return 0;
}
