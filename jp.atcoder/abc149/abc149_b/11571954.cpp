#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  long long a, b, k;
  cin >> a >> b >> k;
  if (k <= a) {
    a -= k;
  } else {
    k -= a;
    a = 0;
    b = max((long long)0, b - k);
  }
  cout << a << ' ' << b << '\n';
  return 0;
}
