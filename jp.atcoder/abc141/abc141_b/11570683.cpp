#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;
  string ans = "Yes";
  for (int i = 0; i < s.size(); i++) {
    if (i & 1 && s[i] == 'R' || !(i & 1) && s[i] == 'L') {
      ans = "No";
      break;
    }
  }
  cout << ans << '\n';
  return 0;
}
