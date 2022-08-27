#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long a, b, x;
  cin >> a >> b >> x;
  int l = 1;
  long p = 1;
  while(true) {
    if(a * p + b * l > x) break;
    p *= 10;
    l++;
  }
  l--;
  if(!l) {
    cout << 0 << endl;
    return 0;
  }
  long n = min(p - 1, (x - b * l) / a);
  cout << min(n, 1000000000l) << endl;
}
