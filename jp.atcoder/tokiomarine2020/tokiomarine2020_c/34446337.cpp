#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  cin >> n >> k;
  k = min(k, 19);
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  while(k--) {
    vector<int> b(n);
    for(int i = 0; i < n; i++) {
      int l = max(i - a[i], 0);
      int r = min(i + a[i] + 1, n);
      b[l]++;
      if(r < n) b[r]--;
    }
    for(int i = 0; i < n - 1; i++) b[i + 1] += b[i];
    swap(a, b);
  }
  for(int i = 0; i < n; i++) cout << a[i] << " \n"[i == n - 1];
}
