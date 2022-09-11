#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  // parity
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int s = 0;
  for(auto& x: a) s += x & 1;
  if(s == 0 || s == n) {
    cout << 1 << endl;
    return 0;
  }
  sort(a.begin(), a.end());
  vector<int> d(n);
  for(int i = 0; i < n; i++) d[i] = a[i] - a[0];
  int g = 0;
  for(auto& x: d) g = gcd(g, x);
  cout << (g == 1 ? 2 : 1) << endl;
}
