#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  string s;
  cin >> s;
  while(true) {
    s = s.substr(0, s.size() - 1);
    int n = s.size();
    if(n & 1) continue;
    bool ok = true;
    for(int i = 0; i < n / 2; i++) {
      if(s[i] != s[n / 2 + i]) ok = false;
    }
    if(ok) {
      cout << n << endl;
      return 0;
    }
  }
}
