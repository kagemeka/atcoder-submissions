#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<long> x(n), y(n);
  for(int i = 0; i < n; i++) cin >> x[i] >> y[i];
  int cnt = n * (n - 1) * (n - 2) / 6;
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < i; j++) {
      for(int k = 0; k < j; k++) {
        cnt -= (y[j] - y[i]) * (x[k] - x[j]) == (y[k] - y[j]) * (x[j] - x[i]);
      }
    }
  }
  cout << cnt << endl;
}
