#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<long> a(n);
  int sign = -1;
  for(int t = 0; t < 2; t++) {
    for(int i = 0; i < n; i++) {
      int x;
      cin >> x;
      a[i] += sign * x;
    }
    sign *= -1;
  }
  sort(a.rbegin(), a.rend());
  long buf = 0;
  for(auto& x: a) {
    long c = max((x + 1) / 2, 0l);
    x -= c * 2;
    buf += c;
    if(x == 0) continue;
    if(-x > buf) {
      cout << "No" << endl;
      return 0;
    }
    buf += x;
  }
  cout << "Yes" << endl;
}
