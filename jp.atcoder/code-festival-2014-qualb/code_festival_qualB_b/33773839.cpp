#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  cin >> n >> k;
  vector<int> a(n);
  int s = 0;
  for(int i = 0; i < n; i++) cin >> a[i];
  for(int i = 0; i < n; i++) {
    s += a[i];
    if(s >= k) {
      cout << i + 1 << endl;
      return 0;
    }
  }
}
