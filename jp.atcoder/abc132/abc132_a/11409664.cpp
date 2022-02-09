#include <bits/stdc++.h>
using namespace std;

int main() {
  string s;
  cin >> s;
  sort(s.begin(), s.end());
  string ans = (s[0] == s[1] && s[1] != s[2] && s[2] == s[3]) ? "Yes" : "No";
  cout << ans << endl;
  return 0;
}
