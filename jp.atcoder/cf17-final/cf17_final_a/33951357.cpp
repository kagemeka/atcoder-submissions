#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s;
  cin >> s;
  int n = s.size();
  string t = "AKIHABARA";
  int m = t.size();
  bool ok = true;
  for(int i = 0, j = 0; i < n; i++) {
    while(j < m && s[i] != t[j] && t[j] == 'A') { j++; }
    if(j == m || s[i] != t[j]) {
      ok = false;
      break;
    }
    j++;
  }
  cout << (ok ? "YES" : "NO") << endl;
}
