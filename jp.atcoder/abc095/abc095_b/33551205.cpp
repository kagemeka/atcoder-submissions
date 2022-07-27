#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, x;
  cin >> n >> x;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int s = accumulate(a.begin(), a.end(), 0);
  x -= s;
  cout << n + (x / *min_element(a.begin(), a.end())) << endl;
}
