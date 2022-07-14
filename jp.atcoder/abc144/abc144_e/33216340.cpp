#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  long k;
  cin >> n >> k;
  vector<long> a(n), f(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  for(int i = 0; i < n; i++) cin >> f[i];
  sort(a.begin(), a.end());
  sort(f.rbegin(), f.rend());
  auto possible = [&](long x) -> bool {
    long cnt = 0;
    for(int i = 0; i < n; i++) { cnt += max(0l, a[i] - x / f[i]); }
    return cnt <= k;
  };
  long ng = -1, ok = 1l << 40;
  while(ok - ng > 1) {
    long x = (ng + ok) >> 1;
    if(possible(x)) ok = x;
    else ng = x;
  }
  cout << ok << endl;
}
