#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n + 1);
  for(int i = 0; i < n; i++) {
    cin >> a[i + 1];
    a[i + 1] += a[i];
  }
  int tot = a[n];
  if(tot % n) {
    cout << -1 << endl;
    return 0;
  }
  int m = tot / n;
  int cnt = 0;
  for(int l = 0; l < n;) {
    int r = l + 1;
    while(true) {
      if(a[r] - a[l] == m * (r - l)) break;
      r++;
    }
    cnt += r - l - 1;
    l = r;
  }
  cout << cnt << endl;
}
