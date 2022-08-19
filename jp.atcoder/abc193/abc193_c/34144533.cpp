#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long n;
  cin >> n;
  int const k = 1 << 17;
  vector<bool> searched(k);
  long cnt = 0;
  for(long i = 2; i * i <= n; i++) {
    if(searched[i]) continue;
    long p = i * i;
    while(p <= n) {
      cnt++;
      if(p < k) searched[p] = true;
      p *= i;
    }
  }
  cout << n - cnt << endl;
}
