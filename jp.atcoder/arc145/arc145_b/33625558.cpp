#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  long n, a, b;
  cin >> n >> a >> b;
  if(a <= b) {
        cout << n - (a - 1) << endl;
    return 0;
  }
  long q = n / a;
  n %= a;
  long res;
  if(q > 0) {
    res = (q - 1) * b + min(n + 1, b);
  } else {
    res = 0;
  }
  cout << res << endl;
}
