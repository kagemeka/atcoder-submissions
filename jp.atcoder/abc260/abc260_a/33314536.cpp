#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  string s;
  cin >> s;
  sort(s.begin(), s.end());
  if(s[0] != s[1]) {
    cout << s[0] << endl;
  } else if(s[1] != s[2]) {
    cout << s[2] << endl;
  } else {
    cout << -1 << endl;
  }
}
