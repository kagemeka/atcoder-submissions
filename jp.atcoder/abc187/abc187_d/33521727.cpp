#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  long s = 0;
  vector<long> a(n);
  for(int i = 0; i < n; i++) {
    long x, y;
    cin >> x >> y;
    s -= x;
    a[i] = 2 * x + y;
  }
  sort(a.rbegin(), a.rend());
  for(int i = 0; i < n; i++) {
    s += a[i];
    if(s <= 0) continue;
    cout << i + 1 << endl;
    return 0;
  }
}
