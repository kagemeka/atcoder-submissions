#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  for(int i = n; i >= 1; i--) {
    for(int j = i * 2; j <= n; j += i) { a[i - 1] ^= a[j - 1]; }
  }
  cout << accumulate(a.begin(), a.end(), 0) << endl;
  for(int i = 0; i < n; i++) {
    if(a[i] & 1) { cout << i + 1 << endl; }
  }
}
