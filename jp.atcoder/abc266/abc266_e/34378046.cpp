#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<double> ex(n + 1);
  ex[n] = 3.5;
  for(int i = n - 1; i >= 1; i--) {
    double x = ex[i + 1];
    double& y = ex[i];
    for(int j = 1; j <= 6; j++) {
      double k = j;
      y += max(k, x);
    }
    y /= 6;
  }
  cout << setprecision(16) << ex[1] << endl;
}
