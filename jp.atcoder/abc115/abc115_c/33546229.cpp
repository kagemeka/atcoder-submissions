#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  cin >> n >> k;
  vector<long> h(n);
  for(int i = 0; i < n; i++) cin >> h[i];
  sort(h.begin(), h.end());
  long mn = 1l << 60;
  for(int i = 0; i < n - k + 1; i++) { mn = min(mn, h[i + k - 1] - h[i]); }
  cout << mn << endl;
}
