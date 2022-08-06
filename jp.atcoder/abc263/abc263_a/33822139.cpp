#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  vector<int> a(5);
  for(int i = 0; i < 5; i++) cin >> a[i];
  bool ok;
  sort(a.begin(), a.end());
  ok = a[0] == a[1] && a[1] == a[2] && a[2] != a[3] && a[3] == a[4];
  ok = ok || (a[0] == a[1] && a[1] != a[2] && a[2] == a[3] && a[3] == a[4]);
  cout << (ok ? "Yes" : "No") << endl;
}
