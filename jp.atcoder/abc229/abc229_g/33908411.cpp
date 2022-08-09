#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s;
  long k;
  cin >> s >> k;
  vector<int> a;
  for(int i = 0; i < (int)s.size(); i++)
    if(s[i] == 'Y') a.push_back(i);
  int n = a.size();
  int mx = 0;
  long sum = 0;
  for(int l = 0, r = 0; l < n; l++) {
    while(r < n) {
      int i = (r - l) >> 1;
      int m = l + i;
      long s = sum + a[r] - a[m] - (r - m);
      if(s <= k) {
        sum = s;
        r++;
      } else {
        break;
      }
    }
    mx = max(mx, r - l);
    int i = (r - l) >> 1;
    int m = l + i;
    sum -= a[m] - a[l] - i;
  }
  cout << mx << endl;
}
