#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  string s;
  cin >> n >> s;
  int l = 0, r = 0;
  for(auto& c: s) {
    if(c == '(') {
      l++;
    } else {
      if(l) l--;
      else r++;
    }
  }
  cout << string(r, '(') << s << string(l, ')') << endl;
}
