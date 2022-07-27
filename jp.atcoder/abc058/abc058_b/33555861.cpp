#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s, t;
  cin >> s >> t;
  int n = s.size(), m = t.size();
  string res = "";
  for(int i = 0; i < m; i++) {
    res += s[i];
    res += t[i];
  }
  if(n != m) res += s[n - 1];
  cout << res << endl;
}
