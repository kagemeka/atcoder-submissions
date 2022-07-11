#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<long> a(n);
  int sign = 1;
  for(int t = 0; t < 2; t++) {
    for(int i = 0; i < n; i++) {
      int x;
      cin >> x;
      a[i] += sign * x;
    }
    sign *= -1;
  }
  int add = 0;
  int sub = 0;
  for(auto& x: a) {
    if(x > 0) {
      sub += x;
    } else {
      sub += x & 1;
      add += (-x + 1) >> 1;
    }
  }
  cout << (add >= sub ? "Yes" : "No") << endl;
}
