#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  int r = n;
  for(int i = 0; i < m; i++) {
    if((r - 1 - i) * 2 == n) r--;
    cout << i + 1 << ' ' << r << endl;
    r--;
  }
}
