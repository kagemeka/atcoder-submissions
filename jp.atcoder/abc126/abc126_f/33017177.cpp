#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int m, k;
  cin >> m >> k;

  if(k >= 1 << m) {
    cout << -1 << endl;
    return 0;
  }
  if(m == 1) {
    if(k == 1) {
      cout << -1 << endl;
    } else {
      cout << 1 << ' ' << 1 << ' ' << 0 << ' ' << 0 << endl;
    }
    return 0;
  }

  vector<int> res;
  res.push_back(k);
  for(int i = 0; i < 1 << m; i++) {
    if(i == k) continue;
    res.push_back(i);
  }
  res.push_back(k);
  for(int i = 1 << m; i > 0; i--) {
    if(i - 1 == k) continue;
    res.push_back(i - 1);
  }
  int n = res.size();
  for(int i = 0; i < n; i++) { cout << res[i] << " \n"[i == n - 1]; }
}
