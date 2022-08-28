#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  long s = 0;
  long t = 0;
  for(auto& x: a) {
    s += x;
    t += x * x;
  }
  cout << n * t - s * s << endl;
}
