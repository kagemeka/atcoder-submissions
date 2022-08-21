#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int m, n, k;
  cin >> m >> n >> k;
  int cnt = k;
  while(true) {
    int q = k / m;
    if(q == 0) break;
    int r = k % m;
    k = q * n;
    cnt += k;
    k += r;
  }
  cout << cnt << endl;
}
