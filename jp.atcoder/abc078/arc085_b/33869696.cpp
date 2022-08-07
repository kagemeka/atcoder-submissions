#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, z, w;
  cin >> n >> z >> w;
  // game simulatation
  // take n or n - 1;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int res = abs(a[n - 1] - w);
  if(n > 1) res = max(res, abs(a[n - 1] - a[n - 2]));
  cout << res << endl;
}
