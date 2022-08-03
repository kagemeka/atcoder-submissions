#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n), b(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  for(int i = 0; i < n; i++) cin >> b[i];
  vector<int> d(n);
  for(int i = 0; i < n; i++) d[i] = a[i] - b[i];
  long x = 0, y = 0;
  for(auto& d: d) {
    if(d >= 0) {
      x += d;
    } else {
      y += d / 2;
    }
  }
  cout << (x + y > 0 ? "No" : "Yes") << endl;
}
