#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<vector<int>> a(2, vector<int>(n));
  for(int i = 0; i < 2; i++) {
    for(int j = 0; j < n; j++) {
      int& x = a[i][j];
      cin >> x;
      int mx = 0;
      if(i == 1) { mx = max(mx, a[0][j]); }
      if(j > 0) { mx = max(mx, a[i][j - 1]); }
      x += mx;
    }
  }
  cout << a[1][n - 1] << endl;
}
