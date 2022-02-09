#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  int t;
  cin >> s >> t;

  int cnt = 0;
  int x = 0, y = 0;
  for (char &c : s) {
    if (c == '?') cnt++;
    else if (c == 'L') x--;
    else if (c == 'R') x++;
    else if (c == 'U') y++;
    else if (c == 'D') y--;
  }
  int d = abs(x) + abs(y);
  int ans = (t == 1) ? d + cnt : max((d - cnt) & 1, (d - cnt));
  cout << ans << '\n';
  return 0;
}
