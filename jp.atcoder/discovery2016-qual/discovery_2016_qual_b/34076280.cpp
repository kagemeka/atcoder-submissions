#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int const inf = 1 << 30;
  reverse(a.begin(), a.end());
  vector<int> b(n, inf);
  bool flg = false;
  for(int i = 0; i < n; i++) {
    int x = a[i];
    auto it = lower_bound(b.begin(), b.end(), x);
    if(i == n - 1 && *it == inf) flg = true;
    *it = x;
  }
  cout << lower_bound(b.begin(), b.end(), inf) - b.begin() - flg << endl;
}
