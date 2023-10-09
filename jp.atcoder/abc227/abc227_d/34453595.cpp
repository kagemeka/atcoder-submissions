#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  cin >> n >> k;
  vector<long> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  sort(a.begin(), a.end());
  long s = 0;
  int i = 0;
  while(i < n - k + 1) {
    s += a[i];
    i++;
  }
  int c = 1;
  while(i < n) {
    long x = s / c;
    if (x < a[i]) {
      cout << x << endl;
      return 0;
    }
    s += a[i];
    i++;
    c++;
  }
  cout << s / c << endl;
}
