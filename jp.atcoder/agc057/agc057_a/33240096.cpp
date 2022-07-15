#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int t;
  cin >> t;
  while(t--) {
    int l, r;
    cin >> l >> r;
    auto rs = to_string(r);
    int len = rs.size();
    int x;
    if(len == 1) {
      x = 0;
    } else {
      if(rs[0] == '1') {
        x = max(stoi(rs.substr(0, len - 1)), stoi(rs.substr(1, len - 1)));
      } else {
        x = pow(10, len - 1) - 1;
      }
    }
    cout << r - max(x, l - 1) << endl;
  }
}
