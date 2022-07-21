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
    int idx = n;
    for(auto& t: s) { idx = min(idx, (int)t.find_first_of('0')); }
    string res = "";
    res += string(idx, '1');
    res += '0';
    res += string(2 * n - idx, '1');
    cout << res << endl;
  }
}
