#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n = 4;
  vector<int> x(n), y(n);
  for(int i = 0; i < n; i++) cin >> x[i] >> y[i];
  auto ok = [&](int i, int j, int k) -> bool {
    int v = (x[j] - x[i]) * (y[k] - y[i]) - (x[k] - x[i]) * (y[j] - y[i]);
    return v < 0;
  };
  for(int i = 0; i < n; i++) {
    int j = (i + n - 1) % n;
    int k = (i + 1) % n;
    if(ok(i, j, k)) continue;
    cout << "No" << endl;
    return 0;
  }
  cout << "Yes" << endl;
}
