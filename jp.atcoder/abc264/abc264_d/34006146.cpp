#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s;
  cin >> s;
  int n = s.size();
  string t = "atcoder";
  int cnt = 0;
  for(int i = 0; i < n; i++) {
    for(int j = i; j < n; j++) {
      if(s[j] == t[i]) {
        for(int k = j; k > i; k--) {
          swap(s[k], s[k - 1]);
          cnt++;
        }
        break;
      }
    }
  }
  assert(s == t);
  cout << cnt << endl;
}
