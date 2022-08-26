#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  long a, b;
  cin >> n >> a >> b;
  vector<long> x(n);
  for(int i = 0; i < n; i++) cin >> x[i];
  long s = 0;
  for(int i = 0; i < n - 1; i++) { s += min(b, (x[i + 1] - x[i]) * a); }
  cout << s << endl;
}
