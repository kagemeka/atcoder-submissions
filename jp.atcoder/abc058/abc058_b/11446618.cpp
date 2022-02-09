#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s, t;
  cin >> s >> t;

  int n = s.size();
  string res = "";
  for (int i = 0; i < n; i++) {
    res += s[i];
    if (i != n - 1) res += t[i];
    else if (t.size() == n) res += t[i];
  }
  cout << res << '\n';
  return 0;
}
