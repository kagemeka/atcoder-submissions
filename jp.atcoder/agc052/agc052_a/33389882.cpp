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
    cout << string(n, '0') + string(n, '1') + '0' << endl;
  }
}
