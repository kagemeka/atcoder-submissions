#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  long t;
  cin >> n >> m >> t;
  vector<long> a(n - 1);
  for(int i = 0; i < n - 1; i++) cin >> a[i];
  vector<long> bonus(n + 10);
  for(int i = 0; i < m; i++) {
    int x, y;
    cin >> x >> y;
    x--;
    bonus[x] = y;
  }
  for(int i = 0; i < n - 1; i++) {
    t += bonus[i];
    if(t <= a[i]) {
      cout << "No" << endl;
      return 0;
    }
    t -= a[i];
  }
  cout << "Yes" << endl;
}
