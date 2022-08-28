#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k, m;
  cin >> n >> k >> m;
  int s = 0;
  for(int i = 0; i < n - 1; i++) {
    int x;
    cin >> x;
    s += x;
  }
  int d = max(0, n * m - s);
  cout << (d > k ? -1 : d) << endl;
}
