#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long n;
  cin >> n;
  long const mod = 998244353;
  long cnt = 0;
  for(long i = 1; i * i <= n; i++) {
    long j = n / i;
    cnt += 1 + (j - i) / 2;
  }
  cout << cnt % mod << endl;
}
