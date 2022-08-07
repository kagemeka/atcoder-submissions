#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  vector<int> prev(n, -1);
  vector<bool> ok(n + 1, false);
  for(int i = 0; i < n; i++) {
    int x = a[i];
    if(i - prev[x] > m) ok[x] = true;
    prev[x] = i;
  }
  for(int i = 0; i <= n; i++) {
    if(n - prev[i] > m) ok[i] = true;
    if(ok[i]) {
      cout << i << endl;
      return 0;
    }
  }
}
