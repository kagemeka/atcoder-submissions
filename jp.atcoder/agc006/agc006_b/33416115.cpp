#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, x;
  cin >> n >> x;
  x--;
  int m = 2 * n - 1;
  if(x == 0 || x == m - 1) {
    cout << "No" << endl;
    return 0;
  }
  cout << "Yes" << endl;
  vector<int> p(m);
  for(int i = 0; i < m; i++) p[i] = i;
  if(n > 2) {
    swap(p[n - 1], p[x]);
    if(x == 1) {
      swap(p[n], p[x - 1]);
      swap(p[n - 2], p[x + 1]);
      swap(p[n + 1], p[x + 2]);
    } else {
      swap(p[n], p[x + 1]);
      swap(p[n - 2], p[x - 1]);
      swap(p[n + 1], p[x - 2]);
    }
  }
  for(int i = 0; i < m; i++) { cout << p[i] + 1 << endl; }
}
