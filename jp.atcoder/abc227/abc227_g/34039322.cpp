#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long n, k;
  cin >> n >> k;
  long x = n - k + 1;
  vector<long> a(k + 1), b(k + 1);
  for(int i = 0; i < k + 1; i++) {
    a[i] = i;
    b[i] = i + x;
  }
  long res = 1;
  long const mod = 998244353;
  for(int i = 2; i <= k; i++) {
    if(a[i] == 1) continue;
    int e = 0;
    for(int j = i; j <= k; j += i) {
      while(a[j] % i == 0) {
        e--;
        a[j] /= i;
      }
    }
    for(long j = (x + i - 1) / i * i; j <= n; j += i) {
      assert(x <= j && j <= n);
      int l = j - x;
      while(b[l] % i == 0) {
        e++;
        b[l] /= i;
      }
    }
    assert(e >= 0);
    res *= (e + 1);
    res %= mod;
  }
  for(int i = 0; i < k; i++) {
    if(b[i] != 1) {
      res *= 2;
      res %= mod;
    }
  }
  cout << res << endl;
}
