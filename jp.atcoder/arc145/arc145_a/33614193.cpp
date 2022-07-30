#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  string s;
  cin >> s;
  if(n == 2) {
    cout << (s[0] == s[1] ? "Yes" : "No") << endl;
    return 0;
  }
  cout << (s[0] == 'A' && s[n - 1] == 'B' ? "No" : "Yes") << endl;
}
