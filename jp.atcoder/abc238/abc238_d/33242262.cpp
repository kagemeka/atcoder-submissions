#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int t;
  cin >> t;
  while(t--) {
    long a, s;
    cin >> a >> s;
    long x = s - 2 * a;
    cout << (0 <= x && x <= s ? "Yes" : "No") << endl;
  }
}
