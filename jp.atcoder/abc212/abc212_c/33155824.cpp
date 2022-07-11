#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  vector<int> a(n), b(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  for(int i = 0; i < n; i++) cin >> b[i];
  sort(a.begin(), a.end());
  sort(b.begin(), b.end());
  int mn = (1l << 31) - 1;
  for(int i = 0, j = 0; i < n; i++) {
    while(j < n && b[j] <= a[i]) {
      mn = min(mn, a[i] - b[j]);
      j++;
    }
    if(j < n) { mn = min(mn, abs(a[i] - b[j])); }
  }
  cout << mn << endl;
}
