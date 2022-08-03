#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  vector<long> a(3);
  for(int i = 0; i < 3; i++) cin >> a[i];
  sort(a.begin(), a.end());
  int k;
  cin >> k;
  cout << a[0] + a[1] + (a[2] << k) << endl;
}
