#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s, t;
  cin >> s >> t;
  string ans = "No";
  for (int i = 0; i < s.size(); i++) {
    if (s == t) {
      ans = "Yes";
      break;
    }
    s = s.substr(1) + s[0];
  }
  cout << ans << '\n';
  return 0;
}
