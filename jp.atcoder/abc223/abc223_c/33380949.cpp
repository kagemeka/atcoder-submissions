#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<double> a(n), b(n);
  for(int i = 0; i < n; i++) cin >> a[i] >> b[i];
  double t = 0;
  for(int i = 0; i < n; i++) t += a[i] / b[i];
  t /= 2;
  double l = 0;
  for(int i = 0; i < n; i++) {
    double dt = a[i] / b[i];
    if(t - dt >= 0) {
      t -= dt;
      l += a[i];
      continue;
    }
    l += b[i] * t;
    break;
  }
  cout << setprecision(16) << l << endl;
}
