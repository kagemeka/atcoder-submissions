#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, a, b;
  string s;
  cin >> n >> a >> b >> s;
  int sab = 0, sb = 0;
  for(int i = 0; i < n; i++) {
    if(s[i] == 'c' || sab >= a + b || (s[i] == 'b' && sb >= b)) {
      cout << "No" << endl;
      continue;
    }
    cout << "Yes" << endl;
    sab++;
    sb += s[i] == 'b';
  }
}
