#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n), b(n), c(n);
  for(int i = 0; i < n; i++) {
    cin >> a[i];
    a[i]--;
  }
  for(int i = 0; i < n; i++) {
    cin >> b[i];
    b[i]--;
  }
  for(int i = 0; i < n; i++) {
    cin >> c[i];
    c[i]--;
  }
  vector<int> cnt(n);
  for(auto& x: a) cnt[x]++;
  long res = 0;
  for(auto& c: c) { res += cnt[b[c]]; }
  cout << res << endl;
}
