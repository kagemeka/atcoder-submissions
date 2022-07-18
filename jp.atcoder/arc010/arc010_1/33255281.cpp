#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m, a, b;
  cin >> n >> m >> a >> b;
  vector<int> c(m);
  for(int i = 0; i < m; i++) cin >> c[i];
  for(int i = 0; i < m; i++) {
    if(n <= a) n += b;
    n -= c[i];
    if(n < 0) {
      cout << i + 1 << endl;
      return 0;
    }
  }
  cout << "complete" << endl;
}
