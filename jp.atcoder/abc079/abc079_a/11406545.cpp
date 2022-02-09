#include <bits/stdc++.h>
using namespace std;

int main() {
  string s;
  cin >> s;
  string ans = "No";
  if (s[1] == s[2]) {
    if (s[0] == s[1] || s[2] == s[3]) ans = "Yes";
  }
  cout << ans << endl;
  return 0;
}
