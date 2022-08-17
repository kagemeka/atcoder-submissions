#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<pair<int, int>> a(n);
  for(int i = 0; i < n; i++) {
    int x, d;
    cin >> x >> d;
    int l = x - d;
    int r = x + d;
    a[i] = {r, l};
  }
  sort(a.begin(), a.end());
  int const inf = 1 << 30;
  int x = -inf;
  int cnt = 0;
  for(auto& [r, l]: a) {
    if(l < x) continue;
    x = r;
    cnt++;
  }
  cout << cnt << endl;
}
