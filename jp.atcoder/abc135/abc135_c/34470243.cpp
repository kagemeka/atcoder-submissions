#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n + 1), b(n);
  for (int i = 0; i < n + 1; i++) cin >> a[i];
  for (int i = 0; i < n; i++) cin >> b[i];
  long cnt = 0;
  for (int i = 0; i < n; i++) {
    int d = min(b[i], a[i]);
    a[i] -= d;
    b[i] -= d;
    cnt += d;
    d = min(b[i], a[i + 1]);
    a[i + 1] -= d;
    b[i] -= 1;
    cnt += d;
  }
  cout << cnt << endl;
}
