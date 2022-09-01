#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int k, s;
  cin >> k >> s;
  long res = 0;
  for(int x = 0; x <= k; x++) {
    int t = s - x;
    if(t < 0 || t > 2 * k) continue;
    res += t <= k ? t + 1 : 2 * k - t + 1;
  }
  cout << res << endl;
}
