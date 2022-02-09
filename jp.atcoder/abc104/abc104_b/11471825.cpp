#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;
  int n = s.size();
  bool flag = false;
  if (s[0] != 'A') flag = true;
  else {
    int cnt = 0;
    for (char &c : s) {
      if (c != 'C' && c != 'A') {
        if ('a' <= c && c <= 'z') continue;
        flag = true;
        break;
      }
    }
    if (!flag) {
      for (char &c : s.substr(2, n - 3)) {
        cnt += c == 'C';
      }
      if (cnt != 1) flag = true;
    }
  }
  string ans = flag ? "WA" : "AC";
  cout << ans << '\n';
  return 0;
}
