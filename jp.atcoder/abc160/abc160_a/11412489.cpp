#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;

  string ans = (s[2] == s[3] && s[4] == s[5]) ? "Yes" : "No";
  cout << ans << endl;
  return 0;

}
