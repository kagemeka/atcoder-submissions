#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, t;
  cin >> n >> t;
  vector<int> a(n), b(n);
  for(int i = 0; i < n; i++) cin >> a[i] >> b[i];
  vector<int> d(n);
  for(int i = 0; i < n; i++) d[i] = a[i] - b[i];
  sort(d.rbegin(), d.rend());
  for(auto& x: a) t -= x;
  for(int i = 0; i < n; i++) {
    if(t >= 0) {
      cout << i << endl;
      return 0;
    }
    t += d[i];
  }
  cout << (t >= 0 ? n : -1) << endl;
}
