#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  int m = 1 << n;
  vector<int> c(m - 1);
  for(int i = 0; i < m - 1; i++) cin >> c[i];
  vector<int> idx(m - 1);
  iota(idx.begin(), idx.end(), 0);
  sort(idx.begin(), idx.end(), [&](int i, int j) { return c[i] < c[j]; });
  vector<bool> ok(m);
  ok[0] = true;
  long s = 0;
  for(auto j: idx) {
    int x = c[j];
    j += 1;
    if(ok[j]) continue;
    s += x;
    for(int i = 0; i < m; i++) { ok[i ^ j] = ok[i ^ j] | ok[i]; }
  }
  cout << s << endl;
}
