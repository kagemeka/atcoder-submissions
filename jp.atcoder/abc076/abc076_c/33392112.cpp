#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s, t;
  cin >> s >> t;
  int n = s.size(), m = t.size();
  auto restore = [&](int i) -> string {
    string res = s;
    for(int j = 0; j < m; j++) {
      if(res[i + j] == '?') res[i + j] = t[j];
      else {
        if(res[i + j] != t[j]) { return ""; }
      }
    }
    for(int i = 0; i < n; i++) {
      if(res[i] == '?') res[i] = 'a';
    }
    return res;
  };
  for(int i = n - m; i >= 0; i--) {
    auto res = restore(i);
    if(res != "") {
      cout << res << endl;
      return 0;
    }
  }
  cout << "UNRESTORABLE" << endl;
}
