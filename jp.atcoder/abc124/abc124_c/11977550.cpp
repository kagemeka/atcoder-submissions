#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int c1 = 0, c2 = 0;
  string s;
  cin >> s;
  for (int i = 0; i < s.size(); i++) {
    if (i & 1) {
      c1 += s[i] != '1';
      c2 += s[i] != '0';
    } else {
      c1 += s[i] != '0';
      c2 += s[i] != '1';
    }
  }
  cout << min(c1, c2) << '\n';
  return 0;
}
