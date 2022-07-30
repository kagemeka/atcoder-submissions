#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  long n, a, b;
  cin >> n >> a >> b;
  if(a <= b) {
    cout << n << endl;
    return 0;
  }
  long q = n / a;
  // n %= a;
  // cout << q << ' ' << n << endl;
  long res = q * b;
  cout << res << endl;
}
