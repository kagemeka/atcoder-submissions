#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s;
  cin >> s;
  int n = s.size();
  string t = "AKIHABARA";
  int m = t.size();
  bool ok = true;
  int j = 0;
  for(int i = 0; i < n; i++) {
    while(j < m && s[i] != t[j] && t[j] == 'A') { j++; }
    if(j == m || s[i] != t[j]) {
      ok = false;
      break;
    }
    j++;
  }
  while(j < m && t[j] == 'A') j++;
  ok = ok && j == m;
  cout << (ok ? "YES" : "NO") << endl;
}
