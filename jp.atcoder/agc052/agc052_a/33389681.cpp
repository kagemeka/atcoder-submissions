#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int t;
  cin >> t;
  while(t--) {
    int n;
    cin >> n;
    vector<string> s(3);
    for(int i = 0; i < 3; i++) cin >> s[i];
    int d = 0;
    for(auto& t: s) {
      int i = 0;
      while(t[i] == '0') i++;
      int j = 0;
      while(j < 2 * n && t[j] == '1') j++;
      d = max(d, j - i);
    }
    string res = "";
    res += string(d, '1');
    res += '0';
    res += string(2 * n - d, '1');
    cout << res << endl;
  }
}
