#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<long> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int l = 0;
  int r = n - 1;
  long cnt = 0;
  for(int t = 0; t < n >> 1; t++) {
    long cl = a[l] * 2 + a[l + 1];
    long cr = a[r] * 2 + a[r - 1];
    cnt += min(cl, cr) + 1;
    if(cl <= cr) {
      l += 2;
      a[l] += cl - a[l - 2] + 2;
    } else {
      r -= 2;
      a[r] += cr - a[r + 2] + 2;
    }
  }
  cout << cnt << endl;
}
