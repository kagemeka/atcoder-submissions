#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  string s;
  cin >> n >> k >> s;
  s = '1' + s;
  int cnt = 0;
  int mx = 0;
  for(int l = 1, r = 0; l <= n; l++) {
    if(s[l - 1] == '0' && s[l] == '1') cnt--;
    while(r <= n && cnt <= k) {
      if(r < n && s[r] == '1' && s[r + 1] == '0') cnt++;
      r++;
    }
    mx = max(mx, r - l);
  }
  cout << mx << endl;
}
