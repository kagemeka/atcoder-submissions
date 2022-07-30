#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  string s;
  cin >> s;
  int m = (n - 1) / 2;
  for(int i = 0; i < m; i++) {
    if(s[i] == s[n - 1 - i]) continue;
    if(s[i] == 'A') {
      cout << "No" << endl;
      return 0;
    }
    s[i] = 'A';
    s[i + 1] = 'B';
  }
  // cout << s << endl;
  for(int i = 0; i < n / 2; i++) {
    if(s[i] == s[n - 1 - i]) continue;
    cout << "No" << endl;
    return 0;
  }
  cout << "Yes" << endl;
}
