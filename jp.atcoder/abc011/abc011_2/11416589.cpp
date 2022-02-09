#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;

  string t = "";
  for (int i = 0; i < s.size(); i++) {
    if (i == 0) {
      t += toupper(s[i]);
    } else {
      t += tolower(s[i]);
    }
  }
  cout << t << '\n';
  return 0;
}
