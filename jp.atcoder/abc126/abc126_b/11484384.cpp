#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;
  int y = stoi(s.substr(0, 2));
  int m = stoi(s.substr(2, 2));
  bool a = 1 <= y && y <= 12;
  bool b = 1 <= m && m <= 12;
  string ans;
  if (a) ans = b ? "AMBIGUOUS" : "MMYY";
  else ans = b ? "YYMM" : "NA";
  cout << ans << '\n';
  return 0;
}
