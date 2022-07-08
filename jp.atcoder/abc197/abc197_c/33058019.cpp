#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int mn = 1 << 30;
  for(int s = 0; s < 1 << (n - 1); s++) {
    vector<int> sep{0};
    for(int j = 0; j < n - 1; j++) {
      if(s >> j & 1) sep.push_back(j + 1);
    }
    sep.push_back(n);
    int res = 0;
    for(int k = 0; k < (int)sep.size() - 1; k++) {
      int l = sep[k];
      int r = sep[k + 1];
      int tmp = 0;
      for(int j = l; j < r; j++) { tmp |= a[j]; }
      res ^= tmp;
    }
    mn = min(mn, res);
  }
  cout << mn << endl;
}
