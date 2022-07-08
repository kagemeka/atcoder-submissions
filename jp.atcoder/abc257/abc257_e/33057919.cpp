#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> c(9);
  for(int& i: c) cin >> i;
  int mn = *min_element(c.begin(), c.end());
  int cnt = n / mn;
  string res;
  while(cnt--) {
    for(int j = 9; j > 0; j--) {
      if((long)mn * cnt + c[j - 1] <= n) {
        n -= c[j - 1];
        res += '0' + j;
        break;
      }
    }
  }
  cout << res << endl;
}
