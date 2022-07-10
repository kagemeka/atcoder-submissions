#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n + 1), b(n);
  for(int i = 0; i < n + 1; i++) cin >> a[i];
  for(int i = 0; i < n; i++) cin >> b[i];
  long tot = 0;
  for(int i = 0; i < n; i++) {
    long cnt = min(a[i], b[i]);
    tot += cnt;
    a[i] -= cnt;
    b[i] -= cnt;
    cnt = min(a[i + 1], b[i]);
    tot += cnt;
    a[i + 1] -= cnt;
  }
  cout << tot << endl;
}
