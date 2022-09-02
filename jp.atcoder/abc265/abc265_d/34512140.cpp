#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  long p, q, r;
  cin >> n >> p >> q >> r;
  vector<long> a(n + 1);
  for(int i = 0; i < n; i++) cin >> a[i + 1];
  for(int i = 0; i < n; i++) a[i + 1] += a[i];
  set<long> s;
  for(auto& x: a) s.insert(x);
  for(auto& x: a) {
    bool ok = s.count(p - x) && s.count(p + q - x) && s.count(p + q + r - x);
    if(ok) {
      cout << "Yes" << endl;
      return 0;
    }
  }
  cout << "No" << endl;
}
