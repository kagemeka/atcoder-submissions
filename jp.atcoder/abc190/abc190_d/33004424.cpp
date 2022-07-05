#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  // a = n / k - (k - 1) / 2
  // k is odd and divisor of n;
  // signed.
  long n;
  cin >> n;

  int cnt = 0;
  for(long i = 1; i * i <= n; i++) {
    if(n % i) continue;
    cnt += i & 1;
    cnt += n / i & 1 && i * i != n;
  }
  cnt *= 2;
  cout << cnt << endl;
}
