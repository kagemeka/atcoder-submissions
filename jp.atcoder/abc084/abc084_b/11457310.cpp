#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int a, b;
  string s;
  cin >> a >> b >> s;
  string ans = "Yes";
  if (s[a] != '-') ans = "No";
  else {
    for (int i = 0; i < s.size(); i++) {
      if (i == a) continue;
      int d = s[i] - '0';
      if (d >= 0 && d <= 9) continue;
      ans = "No";
      break;
    }
  }
  cout << ans << '\n';
  return 0;
}
